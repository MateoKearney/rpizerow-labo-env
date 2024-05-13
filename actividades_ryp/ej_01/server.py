import socket  

HOST = ''                 # Symbolic name meaning all available interfaces (representa el server o el cliente (dirección IP))
PORT = 50007              # Arbitrary non-privileged port (son canales de comunicación. 80 para servicio Web, hay puertos reservados para tipos de acciones. Con cualquiera arriba del 1000 están bien)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Aca se crea el socket, mientras se esté cumpliendo lo de abajo. El segundo del paréntesis es para que se puedan hacer operaciones de numeros masivo
    #Ata el socket a una dirección IP y puerto específico
    s.bind((HOST, PORT)) 
    s.listen(1) #Se puede conectar a un solo dispositivo. Tiene que ver con cuantas conexiones permite para luego empezar a rechazarlas
    client, addr = s.accept() #s.accept() es bloqueante. Devuelve socket que representa al cliente y la dirección del cliente (IP)
    with client: #Tiene que ver con la comunicación con el cliente
        print('Connected by', addr)
        while True:
            data = client.recv(1024) #Recive algo y lo guarda en data. El 1204 tiene que ver con la máxima cantidad de bytes que puedo recibir de un saque
            #if not data: break
            client.sendall(data) #Lo que nos llega, lo devuelve 