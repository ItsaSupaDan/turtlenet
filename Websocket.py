import signal, sys
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
 
PORTNUM = 8000
 
class Echo(WebSocket):
 
    def handleMessage(self):
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
        output = input("Command > ")
        print("Sending " + output)
        self.sendMessage(output.lower())
 
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