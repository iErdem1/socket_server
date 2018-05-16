from socket import *
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


server_name = "192.168.1.139"
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((server_name, server_port))

message = client_socket.recv(1024)  # for welcome and authentication info
print(message)

while True:
    try:
        answer = input('Type message:')

        if message[1:9] == "Question":
            answer2 = input("Save an answer? (Y/N):")

            if answer2[0] == 'Y' or answer2[0] == 'y':
                client_socket.send(answer)
            else:
                print("Ok, give your new answer!\n")
                continue
        elif answer == "exit":
            client_socket.close()
            exit(0)
        else:
            client_socket.send(answer)
        cls()  # to clear terminal
        message = client_socket.recv(1024)

        print(message)
    except:
        client_socket.close()
        exit(0)
