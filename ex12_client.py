# Ex 12: TCP / UDP Client  (run this second, in Terminal 2; choose same option as server)
import socket

HOST = "127.0.0.1"
PORT = 5000

print("1. TCP")
print("2. UDP")
choice = int(input("Enter your choice: "))
message = input("Enter message: ")

if choice == 1:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(message.encode())
    print("Server:", client.recv(1024).decode())
    client.close()
elif choice == 2:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(message.encode(), (HOST, PORT))
    data, _ = client.recvfrom(1024)
    print("Server:", data.decode())
    client.close()
else:
    print("Invalid choice")
