import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []
message = []

print("Server has started...")

def clientthread(conn, nickname):
    conn.send("Welcome to this chatroom!".encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print (message)

            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue
                

def remove_nickname(nickname):
 if nickname in nicknames:
     nicknames.remove(nickname)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    print(nickname + "connected!")
    new_thread = Thread(target= clientthread,args=(conn,nickname))
    new_thread.start()


