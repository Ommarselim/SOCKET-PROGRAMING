import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import socket
from time import sleep
import threading
# MAIN GAME WINDOW
window_main = tk.Tk()
window_main.columnconfigure(0,weight=1)
window_main.geometry("600x600+0+400")
window_main.title("Game Client")
your_name = ""
opponent_name = ""
game_round = 0
game_timer = 4
your_choice = ""
opponent_choice = ""
TOTAL_NO_OF_ROUNDS = 5
your_score = 0
opponent_score = 0

# network client
client = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 12345


top_welcome_frame = tk.Frame(window_main)
top_welcome_frame.grid(row=0,column=0)

lbl_name = tk.Label(top_welcome_frame, text="Name:")
lbl_name.grid(row=0,column=0)
ent_name = tk.Entry(top_welcome_frame)
ent_name.grid(row=0,column=1)
btn_connect = tk.Button(top_welcome_frame, text="Connect",command=lambda: connect())
btn_connect.grid(row=0,column=0)

top_message_frame = tk.Frame(window_main)
top_message_frame.grid(row=1,column=0)

lbl_line = tk.Label(top_message_frame,text="***********************************************************",).grid(row=0,column=0)
lbl_welcome = tk.Label(top_message_frame, text="test")
lbl_welcome.grid(row=1,column=0)
lbl_line_server = tk.Label(top_message_frame,text="***********************************************************",)
lbl_line_server.grid_forget()




top_frame = tk.Frame(window_main)
top_frame.grid_forget()

top_left_frame = tk.Frame(top_frame, highlightbackground="green", highlightcolor="green", highlightthickness=1)
top_left_frame.grid(row=0,column=0, padx=(10, 10))

lbl_your_name = tk.Label(top_left_frame, text="Your name: ", font="Helvetica 13 bold")
lbl_your_name.grid(row=0, column=0, padx=5, pady=8)

lbl_your_type = tk.Label(top_left_frame, text="Your type: " , font="Helvetica 13 bold")
lbl_your_type.grid(row=1, column=0, padx=5, pady=8)

lbl_opponent_name = tk.Label(top_left_frame, text="Opponent: " )
lbl_opponent_name.grid(row=2, column=0, padx=5, pady=8)


top_right_frame = tk.Frame(top_frame, highlightbackground="green", highlightcolor="green", highlightthickness=1)
top_right_frame.grid(row=0,column=1, padx=(10, 10))

lbl_game_round = tk.Label(
    top_right_frame,
    text="Game round (x) starts in",
    foreground="blue",
    font="Helvetica 14 bold",
)
lbl_timer = tk.Label(
    top_right_frame, text=" ", font="Helvetica 24 bold", foreground="blue"
)
lbl_game_round.grid(row=0, column=0, padx=5, pady=5)
lbl_timer.grid(row=1, column=0, padx=5, pady=5)


middle_frame = tk.Frame(window_main)
middle_frame.grid_forget()

lbl_line = tk.Label(middle_frame, text="***********************************************************").grid(row=0,column=0)
lbl_line = tk.Label(middle_frame, text="**** GAME LOG ****", font="Helvetica 13 bold", foreground="blue").grid(row=1,column=0)
lbl_line = tk.Label(middle_frame, text="***********************************************************").grid(row=2,column=0)

round_frame = tk.Frame(middle_frame)
round_frame.grid(row=0,column=0)

lbl_round = tk.Label(round_frame, text="Round")
lbl_round.grid(row=0,column=0)
lbl_your_choice = tk.Label(round_frame, text="Your choice: " + "None", font="Helvetica 13 bold")
lbl_your_choice.grid(row=1,column=0)
lbl_opponent_choice = tk.Label(round_frame, text="Opponent choice: " + "None")
lbl_opponent_choice.grid(row=2,column=0)
lbl_result = tk.Label(round_frame, text=" ", foreground="blue", font="Helvetica 14 bold")
lbl_result.grid(row=3,column=0)



final_frame = tk.Frame(middle_frame)
final_frame.grid(row=1,column=0)

lbl_line = tk.Label(final_frame, text="***********************************************************").grid(row=0,column=0)
lbl_final_result = tk.Label(final_frame, text=" ", font="Helvetica 13 bold", foreground="blue")
lbl_final_result.grid(row=1,column=0)
lbl_line = tk.Label(final_frame, text="***********************************************************").grid(row=2,column=0)



button_frame = tk.Frame(window_main)
button_frame.grid(row=6,column=0)


photo_one = PhotoImage(file=r"images/1.png")
photo_two = PhotoImage(file=r"images/2.png")
photo_three = PhotoImage(file=r"images/3.png")
photo_four = PhotoImage(file=r"images/4.png")
photo_five = PhotoImage(file=r"images/5.png")
photo_six = PhotoImage(file=r"images/6.png")
photo_seven = PhotoImage(file=r"images/7.png")
photo_eight = PhotoImage(file=r"images/8.png")
photo_nine = PhotoImage(file=r"images/9.png")
photo_ten = PhotoImage(file=r"images/10.png")


btn_one = tk.Button(
    button_frame,
    text="one",
    command=lambda: choice("1"),
    state=tk.DISABLED,
    image=photo_one,
    bg="red"
)
btn_one.grid(row=0, column=0)

btn_two = tk.Button(
    button_frame,
    text="two",
    command=lambda: choice("2"),
    state=tk.DISABLED,
    image=photo_two,
)
btn_two.grid(row=0, column=1)

btn_three = tk.Button(
    button_frame,
    text="three",
    command=lambda: choice("3"),
    state=tk.DISABLED,
    image=photo_three,
)
btn_three.grid(row=0, column=2)

btn_four = tk.Button(
    button_frame,
    text="four",
    command=lambda: choice("4"),
    state=tk.DISABLED,
    image=photo_four,
)
btn_four.grid(row=0, column=3)

btn_five = tk.Button(
    button_frame,
    text="five",
    command=lambda: choice("5"),
    state=tk.DISABLED,
    image=photo_five,
)
btn_five.grid(row=0, column=4)

btn_six = tk.Button(
    button_frame,
    text="six",
    command=lambda: choice("6"),
    state=tk.DISABLED,
    image=photo_six,
)
btn_six.grid(row=1, column=0)

btn_seven = tk.Button(
    button_frame,
    text="seven",
    command=lambda: choice("7"),
    state=tk.DISABLED,
    image=photo_seven,
)
btn_seven.grid(row=1, column=1)

btn_eight = tk.Button(
    button_frame,
    text="eight",
    command=lambda: choice("8"),
    state=tk.DISABLED,
    image=photo_eight,
)
btn_eight.grid(row=1, column=2)

btn_nine = tk.Button(
    button_frame,
    text="nine",
    command=lambda: choice("9"),
    state=tk.DISABLED,
    image=photo_nine,
)
btn_nine.grid(row=1, column=3)

btn_ten = tk.Button(
    button_frame,
    text="ten",
    command=lambda: choice("10"),
    state=tk.DISABLED,
    image=photo_ten,
)
btn_ten.grid(row=1, column=4)




def game_logic(your_choice, opponent_choice):
    # winner = ""
    # one = "one"
    # two = "two"
    # three = "three"
    # player0 = "you"
    # player1 = "opponent"

    total = int(your_choice) + int(opponent_choice)
    print(total)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"

    # if your_choice == opponent_choice:
    #     winner = "draw"
    # elif your_choice == one:
    #     if opponent_choice == two:
    #         winner = player1
    #     else:
    #         winner = player0
    # elif your_choice == three:
    #     if opponent_choice == one:
    #         winner = player1
    #     else:
    #         winner = player0
    # elif your_choice == two:
    #     if opponent_choice == three:
    #         winner = player1
    #     else:
    #         winner = player0
    # return winner
    


def enable_disable_buttons(todo):
    if todo == "disable":
        btn_one.config(state=tk.DISABLED)
        btn_two.config(state=tk.DISABLED)
        btn_three.config(state=tk.DISABLED)
        btn_four.config(state=tk.DISABLED)
        btn_five.config(state=tk.DISABLED)
        btn_six.config(state=tk.DISABLED)
        btn_seven.config(state=tk.DISABLED)
        btn_eight.config(state=tk.DISABLED)
        btn_nine.config(state=tk.DISABLED)
        btn_ten.config(state=tk.DISABLED)



    else:
        btn_one.config(state=tk.NORMAL)
        btn_two.config(state=tk.NORMAL)
        btn_three.config(state=tk.NORMAL)
        btn_four.config(state=tk.NORMAL)
        btn_five.config(state=tk.NORMAL)
        btn_six.config(state=tk.NORMAL)
        btn_seven.config(state=tk.NORMAL)
        btn_eight.config(state=tk.NORMAL)
        btn_nine.config(state=tk.NORMAL)
        btn_ten.config(state=tk.NORMAL)

def connect():
    
    if len(ent_name.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter your first name <e.g. John>"
        )
    else:
        your_name = ent_name.get()
        lbl_your_name["text"] = "Your name: " + your_name
        connect_to_server(your_name)


def count_down(my_timer, nothing):
    global game_round
    if game_round <= TOTAL_NO_OF_ROUNDS:
        game_round = game_round + 1

    lbl_game_round["text"] = "Game round " + str(game_round) + " starts in"

    while my_timer > 0:
        my_timer = my_timer - 1
        print("game timer is: " + str(my_timer))
        lbl_timer["text"] = my_timer
        sleep(1)

    enable_disable_buttons("enable")
    lbl_round["text"] = "Round - " + str(game_round)
    lbl_final_result["text"] = " "


def choice(arg):
    global your_choice, client, game_round
    your_choice = arg
    lbl_your_choice["text"] = "Your choice: " + your_choice

    if client:
        dataToSend = "Game_Round" + str(game_round) + your_choice
        client.send(dataToSend.encode())
        enable_disable_buttons("disable")


def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR, your_name
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode())  # Send name to server after connecting

        # disable widgets
        btn_connect.config(state=tk.DISABLED)
        ent_name.config(state=tk.DISABLED)
        lbl_name.config(state=tk.DISABLED)
        enable_disable_buttons("disable")

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        tk.messagebox.showerror(
            title="ERROR!!!",
            message="Cannot connect to host: "
            + HOST_ADDR
            + " on port: "
            + str(HOST_PORT)
            + " Server may be Unavailable. Try again later",
        )


def receive_message_from_server(sck, m):
    global your_name, opponent_name, game_round ,your_type
    global your_choice, opponent_choice, your_score, opponent_score

    while True:
        from_server = str(sck.recv(4096).decode())
        print(from_server)

        if not from_server:
            break

        if from_server == "even":
            your_type ="EVEN !"
            lbl_your_type["text"] = ( "YOU ARE: " + your_type )
        if from_server == "odd":
            your_type="ODD !"
            lbl_your_type["text"] = ( "YOU ARE: " + your_type )


        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                lbl_welcome["text"] = (
                    "Server says: Welcome " + your_name + "! Waiting for player 2"
                )
            elif from_server == "welcome2":
                lbl_welcome["text"] = (
                    "Server says: Welcome " + your_name + "! Game will start soon"
                )
            lbl_line_server.grid(row=2,column=0)

        elif from_server.startswith("opponent_name$"):
            opponent_name = from_server.replace("opponent_name$", "")
            lbl_opponent_name["text"] = "Opponent: " + opponent_name
            top_frame.grid(row=2,column=0)
            middle_frame.grid(row=3,column=0)

            # we know two users are connected so game is ready to start
            threading._start_new_thread(count_down, (game_timer, ""))
            lbl_welcome.config(state=tk.DISABLED)
            lbl_line_server.config(state=tk.DISABLED)

        elif from_server.startswith("$opponent_choice"):
            # get the opponent choice from the server
            opponent_choice = from_server.replace("$opponent_choice", "")
            print(your_choice)
            print(opponent_choice)

            # figure out who wins in this round
            who_wins = game_logic(your_choice, opponent_choice)
            round_result = " "
            if who_wins == "even" and your_type =="EVEN !":
                your_score = your_score + 1
                round_result = "WIN"
            elif who_wins == "odd" and your_type== "EVEN !":
                opponent_score = opponent_score + 1
                round_result = "LOSS"

            elif who_wins == "even" and your_type== "ODD !":
                opponent_score = opponent_score + 1
                round_result = "LOSS"
            elif who_wins == "odd" and your_type== "ODD !":
                your_score = your_score + 1
                round_result = "WIN"

            # Update GUI
            lbl_opponent_choice["text"] = "Opponent choice: " + opponent_choice
            lbl_result["text"] = "Result: " + round_result

            # is this the last round e.g. Round 5?
            if game_round == TOTAL_NO_OF_ROUNDS:
                # compute final result
                final_result = ""
                color = ""

                if your_score > opponent_score:
                    final_result = "(You Won!!!)"
                    color = "green"
                elif your_score < opponent_score:
                    final_result = "(You Lost!!!)"
                    color = "red"
                else:
                    final_result = "(Draw!!!)"
                    color = "black"

                lbl_final_result["text"] = (
                    "FINAL RESULT: "
                    + str(your_score)
                    + " - "
                    + str(opponent_score)
                    + " "
                    + final_result
                )
                lbl_final_result.config(foreground=color)

                enable_disable_buttons("disable")
                game_round = 0
                your_score = 0
                opponent_score = 0

            # Start the timer
            threading._start_new_thread(count_down, (game_timer, ""))

    sck.close()


window_main.mainloop()
