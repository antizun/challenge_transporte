import socket


def init_socket():
	# Create a socket object
	s = socket.socket()        
	flag_archive="FALSE" 
	# Define the port on which you want to connect
	port = 12345               
	 
	# connect to the server on local computer
	s.connect(('127.0.0.1', port))
	 
	# receive data from the server and decoding to get the string.
	flag_archive=s.recv(1024).decode()
	print (flag_archive)

# close the connection
#s.close()  