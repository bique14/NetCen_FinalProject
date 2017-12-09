import socket
import sys
import threading

#TA server IP&port
#host : 128.199.83.36
#port : 34260

class mySocket:
    
    def __init__(self,host,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host,port))  
        self.authen()
        self.status()
        self.friend = self.s.recv(4096).decode().split('\n')
        self.printfriend()

    
    def authen(self):
        Userid = '5809680092'
        Password = '0092'
        UserPort = 55555
        UserIP = socket.gethostbyname(socket.gethostname())
        authenmsg = 'USER:'+ Userid +"\nPASS:"+Password+"\nIP:"+UserIP+ \
        "\nPORT:"+str(UserPort)+"\n"
        self.Sending(authenmsg)
    
    def status(self):
        status = self.s.recv(4096).decode().strip(" \n")
        if status == '200 SUCCESS':
            print('Authentication Successed')
        else:
            print('Authentication Denied')
            sys.exit(-1)

    def Sending(self,msg):
        self.s.send(bytes(msg,'utf-8'))

    def printfriend(self):
        print('Friend List\n')
        for friendl in self.friend:
            if friendl != 'END' and friendl != '':
                result = friendl+" (Status : "
                friendline = friendl.split(':')
                if(friendline[1] == '-1'):
                    print(result + 'offline)\n')
                else:
                    print(result + 'online)\n')

    


#starting point
Starto = mySocket('128.199.83.36',34260)