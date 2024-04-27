import socket
import subprocess
from modules import logging, msgLoader
import subprocess


class Client:
    def __init__(self):
        self.server_ip='' # this is the ip of server who send the command it sore for sending output
        self.server_port=5245 # this is the port of server who send the command port is server listener port
        self.log = logging().log # this is the a function write in module.logging class for log the exception
        self.load = msgLoader() # this is the class from module file it make msg proper formate and encrypted
        self.running_job=False # this is the boolean flag to indicate any job is running or not
        self.listener=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # this is the socket for listen broadcast msg on 5246 port
        self.sender=None

    def send(self,data:bytes): # this is the function for sending data to server
        self.sender=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this is the socket for send tcp msg on 5245 port
        if self.server_ip != '': # check any server ip address have or not
            self.sender.connect((self.server_ip, self.server_port)) # connect to server
            try:
                self.sender.sendall(data) # send data to server
            except Exception as e:
                # SECTION 200
                self.log("200", e) # if exception log in log file
            finally:
                self.sender.close() # after that close connection

    def execute(self, comd:str): # the function to execute command
        try:
            self.running_job=True # make running job True
            if comd != '': # if command is not null then pass for execution
                comd=comd.split(' ') # split command making formate for subprocess
                process = subprocess.Popen(comd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) # make a sub process and connect with pipe stdout
                self.send(self.load.load_send("1")) # send start execution code

                for line in process.stdout: # listen the command output 
                    self.send(self.load.load_send(line)) # send the all output to server
                process.wait()

            self.running_job=False # make flag false
            self.send(self.load.load_send("0")) # send end execution code
            self.server_ip=''
        except KeyboardInterrupt as e:
            # section 201
            self.log(201, 'Exiting from system!') # log the exception

    def receive(self): # receive function for the listening broadcast command
        self.listener.bind(('0.0.0.0', 5246)) # listen on ip and port
        while True: # listen every time
            try:
                data, addr = self.listener.recvfrom(1024) # wait for any data
                res = self.load.reload(data) # make data proper format and decrypted or return code or command
                if res != False and not self.running_job: # if response is true and no job is running then allocate the ip to server ip
                    self.server_ip = addr[0] # set the ip
                    self.execute(res)

            except Exception as e:
                # section 202
                self.log(202, e) # if any exception make it log

if __name__ == "__main__":
    while True:
        try:
            Client().receive()
        except KeyboardInterrupt:
            break
        except:
            pass