import tkinter as tk
import socket
import threading
from time import sleep
from tkinter import messagebox


window = tk.Tk()
window.title("Sever main window")
window.geometry("300x320+0+0")
window.configure(bg="#323561")
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)


# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
topFrame.grid(row=0,column=0)


btnStart = tk.Button(topFrame, text="Start",padx=20, command=lambda: start_server())
btnStart.grid(row=0,column=0)


btnStop = tk.Button(topFrame, text="Stop",padx=20, command=lambda: stop_server())
btnStop.grid(row=0,column=1)


lblHost = tk.Label(topFrame, text="Address:    ")
lblHost.grid(row=1,column=0,columnspan=2,sticky="w")
lblPort = tk.Label(topFrame, text="Port:     ")
lblPort.grid(row=2,column=0,columnspan=2,sticky="w")

clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="============= Client List =============").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=10, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(
    yscrollcommand=scrollBar.set,
    background="#234521",
    highlightbackground="grey",
    state="disabled",
)
clientFrame.grid(row=3,column=0,columnspan=2, pady=(5, 10))


server = None
HOST_ADDR = "localhost"
HOST_PORT = 11223
client_name = " "
clients = []
clients_names = []
player_data = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server is listening on port: " + str(HOST_PORT))

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Address: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)

# Stop server function
def stop_server():
    try:
        global server
        server.close()
        print("Server is off --")
        btnStart.config(state=tk.NORMAL)
        btnStop.config(state=tk.DISABLED)
    except:
        messagebox.showinfo("server is down", "off")


def accept_clients(the_server, y):
    while True:
        if len(clients) < 2:
            client, addr = the_server.accept()
            clients.append(client)

            # use a thread so as not to clog the gui thread
            threading._start_new_thread(send_receive_client_message, (client, addr))




# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data, player0, player1

    client_msg = " "

    # send welcome message to client
    client_name = client_connection.recv(4096).decode()

    if len(clients) < 2:
        client_connection.send("welcome1".encode())
    else:
        client_connection.send("welcome2".encode())

    clients_names.append(client_name)
    update_client_names_display(clients_names)  # update client names display

    if len(clients) > 1:
        sleep(1)

        # send opponent name
        clients[0].send(("opponent_name$" + clients_names[1]).encode())
        clients[1].send(("opponent_name$" + clients_names[0]).encode())
        # go to sleep

    while True:
        data = client_connection.recv(4096).decode()
        if not data:
            break

        # get the player choice from received data
        player_choice = data[11 : len(data)]

        msg = {"choice": player_choice, "socket": client_connection}

        if len(player_data) < 2:
            player_data.append(msg)

        if len(player_data) == 2:
            # send player 1 choice to player 2 and vice versa
            dataToSend0 = "$opponent_choice" + player_data[1].get("choice")
            dataToSend1 = "$opponent_choice" + player_data[0].get("choice")
            player_data[0].get("socket").send(dataToSend0.encode())
            player_data[1].get("socket").send(dataToSend1.encode())

            player_data = []
    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display




# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete("1.0", tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c + "\n")
    tkDisplay.config(state=tk.DISABLED)










window.mainloop()
