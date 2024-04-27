import socket
from modules import logging,msgLoader

class Server:
    def __init__(self, ui):
        self.log = logging().log
        self.msgLoader = msgLoader()
        self.ui=ui

        self.broadcast_addr = ('<broadcast>', 5246)
        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('0.0.0.0', 5245)

        self.run=True

    def bind(self):
        try:
            self.server_socket.bind(self.server_address)
            self.server_socket.listen(255)
            while self.run:
                connection, client_address = self.server_socket.accept()
                try:
                    data = connection.recv(1024)
                    if data:
                        data = self.msgLoader.reload_res(client_address[0], data)
                        if self.ui != False:
                            self.ui.show(data)
                    else:
                        break
                finally:
                    connection.close()
        except Exception as e:
            self.log(401, e)
            self.server_socket.close()
            self.broadcast_socket.close()

        except KeyboardInterrupt:
            self.server_socket.close()
    
    def close(self):
        self.run=False
        self.server_socket.close()
        self.broadcast_socket.close()

    def send_btr(self, data:str):
        try:
            print(self.broadcast_addr)
            self.broadcast_socket.sendto(self.msgLoader.load(data), self.broadcast_addr)
            print("sending complete")
        except Exception as e:
            print(e)
            self.log(400, e)
