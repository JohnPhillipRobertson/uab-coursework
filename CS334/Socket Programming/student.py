# I JOHN ROBERTSON Worked Alone
# Setup the client
import socket
import random

listenPort = 3310
socket.setdefaulttimeout(120)
localhost = '127.0.0.1'


# Step 2
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
s1.connect((localhost, listenPort))
s1.send(("jprob").encode())
data1 = int(s1.recv(1024))
s1.close()

print("Step 1 has consummated.")

# Step 3
listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((localhost, data1))
listenSocket.listen(5)
s2, address = listenSocket.accept()
robotIP = address[0]
listenSocket.close()
data2 = s2.recv(1024)

s2.close()

print("Step 2 has consummated.")

# Step 4
s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data2lhs, data2rhs = data2.decode().split(',')
num = random.randrange(5, 10)
s3.sendto(bytes(num), (localhost, int(data2lhs)))
s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s4.bind((localhost, int(data2rhs)))
print("test test")
data3, addr = s4.recvfrom(num*10)
print(data3)

s3.close()
s4.close()

print("Step 3 has consummated.")
exit()
