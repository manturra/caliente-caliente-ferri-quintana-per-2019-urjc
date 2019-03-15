import socket
import random
puerto = 8080
ip = "10.108.33.6"
respuestas = 5

def crea_respuesta(clientsocket):
    numero = random.randint(0,99)
    condicion = True
    while condicion:
        adivina_numero = clientsocket.recv(2048).decode("utf-8")
        if str(numero) == adivina_numero:
            send_message = "Felicidades"
            condicion = False
        elif str(numero-10) < adivina_numero < str(numero+10):
            send_message = "Caliente, caliente."
        elif str(numero-10) > adivina_numero:
            send_message = "Frio, frio por abajo."
        else:
            send_message = "Frio, frio por arriba."
        send_bytes = str.encode(send_message)
        clientsocket.send(send_bytes)
    clientsocket.close()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((ip, puerto))
    serversocket.listen(respuestas)
    while True:
        print("Esperando conexiones en: ",ip,puerto)
        (clientsocket, address) = serversocket.accept()
        crea_respuesta(clientsocket)
except socket.error:
    print("Problemas usando el puerto", puerto, "¿Tienes permiso?")
