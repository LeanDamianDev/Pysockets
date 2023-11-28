import socket
import http
import time 
HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print('iniciando server...')
    print('server con socket de tipo',socket.AF_INET)
    print('esperando respuesta del cliente')
    conn, addr = s.accept()
    with conn:
        print(f'conectado al host{addr}')
        print()
        data = conn.recv(1024)
        print()
        print(data)
print('programa terminado')












