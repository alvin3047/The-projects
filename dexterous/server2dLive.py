import socket
#server
HOST = '192.168.43.166'
PORT = 2055            
s = socket.socket()
s.bind((HOST, PORT))
#s.sendall('Hello, world')
s.listen(5)
c,addr=s.accept()
time=0
with open("sample.txt",'w') as d:
	print("successfully conneccted with ",addr)
	while True:
		#time=time+1
		data = c.recv(1024).decode()#.split('#')
		print(data)
		d.write(str(data))

s.close()
