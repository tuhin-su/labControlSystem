from rich import print
from Server import Server
from threading import Thread

class UI:
    def __init__(self) -> None:
        self.server=Server(ui=self)


    def show(self, data:dict) -> None:
        print(data)

    def listen(self):
        self.server.bind()
    def show_ui(self):
        while True:
            try:
                comd = input("Enter command: ");
                if comd != '':
                    self.server.send_btr(data=comd)
            except KeyboardInterrupt:
                self.server.close()
                break

    def run(self):
        t1=Thread(target=self.listen)
        t2=Thread(target=self.show_ui)
        print("String")
        t1.start()
        self.show_ui()
        

if __name__ == "__main__":
    s=UI()
    s.run()