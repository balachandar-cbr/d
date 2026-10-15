# Ex 12: TCP / UDP Server  (run this first, in Terminal 1)
import socket

HOST = "127.0.0.1"
PORT = 5000

print("Socket Communication")
print("--------------------")
print("1. TCP")
print("2. UDP")
choice = int(input("Enter your choice: "))

if choice == 1:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print("\nTCP Server started")
    print("Waiting for client on port", PORT)
    conn, addr = server.accept()
    print("Client connected:", addr)
    message = conn.recv(1024).decode()
    print("Client:", message)
    reply = input("Enter reply: ")
    conn.send(reply.encode())
    conn.close()
    server.close()
    print("TCP connection closed.")

elif choice == 2:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("\nUDP Server started")
    print("Waiting for message on port", PORT)
    message, addr = server.recvfrom(1024)
    print("Client:", message.decode())
    reply = input("Enter reply: ")
    server.sendto(reply.encode(), addr)
    server.close()
    print("UDP communication completed.")
else:
    print("Invalid choice")
