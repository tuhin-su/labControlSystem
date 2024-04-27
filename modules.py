from json import dumps, loads
from Encryption import EncryptionSystem
import datetime

class msgLoader: # it is a class that make simple information to proper formate for understandable server
    def __init__(self):
        self.en=EncryptionSystem() # make instance of EncryptionSystem

    def load_send(self, out:str) -> bytes: # it is function that make create output data
        data=out.encode()
        return self.en.encrypt(data)
    
    def reload_res(self, addr:str, data:bytes):
        data = self.en.decrypt(data).decode()
        if data == 0:
            data="Job End"
        elif data == 1:
            data="Job Start"
        return {'addr':addr, 'msg': data}

    def load(self, command:str, id:str='LCSDBTSG-900') -> bytes: # it is function that make command to output it basically use by server
        data={
            'id':id,
            'command':command,
        }
        return self.en.encrypt(dumps(data).encode())
    
    def reload(self, msg:bytes) -> dict: # it is function that make command to understandable for client
        msg = loads(self.en.decrypt(msg))
        if msg['id'] == 'LCSDBTSG-900':
            return msg['command']
        return False

class logging: # it is a class that make for storing logs
    try:
        def log(self, section:int, logMsg): # the log function
            with open('/var/log/LCS.log', 'a+') as f: # the path is default /var/log
                f.write(str(datetime.datetime.now())+":<"+str(section)+">:"+str(logMsg)+'\n') # write log whit date time
    except Exception:
        print("Run as sudo")
        pass
