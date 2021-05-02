import signal, sys
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import time
PORTNUM = 8000
class Echo(WebSocket):
 
    def handleMessage(self):
        def checkback(self):
            rawdata = self.data
            try:
                datachunks = rawdata.split(",")
                datatype = datachunks[0].split(" : ")[1]
                if(datatype == "blocksaroundturtle"):
                    print("data type is blocks")
                    c = 0
                
                    if(c == 0 or c == 2):
                        print("\t\t[" + datachunks[3].split(":")[1] + "]\n")
                        print("[" + datachunks[4].split(":")[1] + "]\t\t\t\t[" + datachunks[6].split(":")[1] + "]\n")
                        print("\t\t[" + datachunks[5].split(":")[1] + "]")        
                    else:
                        print("[" + d + "]")
                    c = c +1
                else:
                    print(datachunks)
            except:
                pass
            print(rawdata)
        def forward():
            self.sendMessage("turtle.forward()")
            checkback()
        def up():
            self.sendMessage("turtle.up()")
            checkback()
        def down():
            self.sendMessage("turtle.down()")
            checkback()
        def left():
            self.sendMessage("turtle.turnLeft()")
            checkback()
        def right():
            self.sendMessage("turtle.turnRight()")
            checkback()
        
        output = input("Command > ")
        if output == "forward":
            forward()
        elif output == "up":
            up()
        elif output == "down":
            down()
        elif output == "left":
            left()
        elif output == "right":
            right()
        elif output == "back":
            left()
            left()
            forward()
        else:
            print("Sending " + output)
            self.sendMessage(output)
            checkback()
 
    def handleConnected(self):
        print("Connected")
 
    def handleClose(self):
        print("Disconnected")
    
    
def close_server(signal, frame):
    server.close()
    sys.exit()
 
if __name__ == "__main__":
    print("Websocket server on port %s" % PORTNUM)
    server = SimpleWebSocketServer('0.0.0.0', PORTNUM, Echo)
    signal.signal(signal.SIGINT, close_server)
    server.serveforever()