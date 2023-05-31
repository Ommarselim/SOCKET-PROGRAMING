import socket

def run_client():
    host = '127.0.0.1'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    player_type = client_socket.recv(1024).decode()
    print("You are playing as", player_type)

    while True:
        try:
            number = int(input("Choose a number from 1 to 10: "))
            client_socket.send(str(number).encode())
            response = client_socket.recv(1024).decode()
            if response == "Number received.":
                print("Waiting for the other player...")
                break
            else:
                print(response)
        except ValueError:
            print("Invalid input. Please enter a number.")

    result = client_socket.recv(1024).decode()
    print(result)

    client_socket.close()

run_client()
