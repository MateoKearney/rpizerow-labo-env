import socket

HOST = socket.gethostbyname(socket.gethostname())    # The remote host. Si importa lo que pongo en host. Idealmente se reservaría una dirección de IP. Tengo que tener un mecanismo que me permita encontrar mi server. El host name es el nombre de un disp dentro de una red
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #Se intenta conectar con el servidor
    s.sendall(b'Hello, world') #Una vez conectado se manda el mensaje
    data = s.recv(1024) #Se recibe el mensaje 
print('Received', repr(data)) #Se devuelve el mensaje