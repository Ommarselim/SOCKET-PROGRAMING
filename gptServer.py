import socket
import threading

def evaluate_winner(number1, number2):
    total = number1 + number2
    if total % 2 == 0:
        return "even"
    else:
        return "odd"

def handle_client(client_socket, player_number):
    while True:
        number = int(client_socket.recv(1024).decode())
        if number < 1 or number > 10:
            client_socket.send("Invalid number. Please choose a number between 1 and 10.".encode())
        else:
            client_socket.send("Number received.".encode())
            return number

def handle_game(player1_socket, player2_socket):
    player1_number = handle_client(player1_socket, 1)
    player2_number = handle_client(player2_socket, 2)

    print("Player 1 chose", player1_number)
    print("Player 2 chose", player2_number)

    winner = evaluate_winner(player1_number, player2_number)
    if winner == "even":
        print("The winner is the even player.")
    else:
        print("The winner is the odd player.")

    player1_socket.send(f"the winner is {winner} player".encode())
    player2_socket.send(f"the winner is {winner} player".encode())

    player1_socket.close()
    player2_socket.close()

def run_server():
    host = '127.0.0.1'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server started. Waiting for connections...")

    player1_socket, player1_address = server_socket.accept()
    print("Player 1 connected.")
    player1_socket.send("even".encode())

    player2_socket, player2_address = server_socket.accept()
    print("Player 2 connected.")
    player2_socket.send("odd".encode())

    game_thread = threading.Thread(target=handle_game, args=(player1_socket, player2_socket))
    game_thread.start()

run_server()
