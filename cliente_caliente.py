import socket

puerto = 8080
ip = "10.108.33.6"

def adivino_numero(cliente):
    condicion = True
    while condicion:
        adivina_numero = input("Introduce un numero del 0 al 99: ")
        send_bytes = str.encode(adivina_numero)
        cliente.send(send_bytes)
        mensaje = cliente.recv(2048).decode("utf-8")
        if mensaje == "Felicidades":
            condicion = False
        print(mensaje)
    cliente.close()
try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip, puerto))
    adivino_numero(cliente)
except OError:
    print("Socket está usándose.")
    cliente.close
