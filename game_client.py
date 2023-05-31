import tkinter as tk
from tkinter import messagebox
import socket
from tkinter import *
from time import sleep
import threading

# MAIN GAME WINDOW
window_main = tk.Tk()
window_main.title("Game Client")
window_main.geometry("400x600")
window_main.configure(bg="#FFF8D6")

your_name = ""
opponent_name = ""
game_round = 0
game_timer = 5
your_choice = ""
opponent_choice = ""
TOTAL_NO_OF_ROUNDS = 5
your_score = 0
opponent_score = 0

# Network client
client = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 7002

top_welcome_frame = tk.Frame(window_main, bg="blue")
top_welcome_frame.pack(side=tk.TOP, pady=10)

lbl_main = tk.Label(top_welcome_frame, text="BY OSAMA AYMAN EL-SAYED", fg="white", bg="blue")
lbl_main.grid(row=0, column=1, pady=5)

lbl_name = tk.Label(top_welcome_frame, text="Name:", font=("Arial", 10), fg="white", bg="blue")
lbl_name.grid(row=2, column=0, pady=5)

ent_name = tk.Entry(top_welcome_frame, font=("Arial", 10))
ent_name.grid(row=2, column=1, pady=5)

btn_connect = tk.Button(top_welcome_frame, text="Connect", font=("Arial", 10), fg="white", bg="blue", command=lambda: connect())
btn_connect.grid(row=2, column=2, pady=(0, 5))

top_message_frame = tk.Frame(window_main)
lbl_line_server = tk.Label(top_message_frame, text="", bg="#FFF8D6")
lbl_line_server.pack_forget()
lbl_welcome = tk.Label(top_message_frame, text="", bg="#FFF8D6")
lbl_welcome.pack()
top_message_frame.pack(side=tk.TOP)

top_frame = tk.Frame(window_main, bg="#FFF8D6")
top_frame.pack(pady=20)

lbl_line = tk.Label(top_frame, text="____________________________________________________", fg="black")
lbl_line.pack(pady=(0, 5))

lbl_line = tk.Label(top_frame, text="GAME INFORMATION", fg="green", font=("Arial", 12, "bold"), bg="#FFF8D6")
lbl_line.pack(pady=(0, 5))

top_left_frame = tk.Frame(top_frame, highlightbackground="green", highlightcolor="white", bg="#FFF8D6", highlightthickness=1)
lbl_your_name = tk.Label(top_left_frame, text="Your name: " + your_name, font="Arial 10 bold", fg='black', bg="#FFF8D6")
lbl_opponent_name = tk.Label(top_left_frame, text="Opponent: " + opponent_name, fg='black', bg="#FFF8D6")
lbl_your_name.grid(row=0, column=0, padx=3, pady=5)
lbl_opponent_name.grid(row=1, column=0, padx=3, pady=5)
top_left_frame.pack(side=tk.LEFT, padx=(10, 10))

top_right_frame = tk.Frame(top_frame, highlightbackground="green", highlightcolor="white", bg="#FFF8D6", highlightthickness=1)
lbl_game_round = tk.Label(top_right_frame, text="Game round (x) starts in", foreground="black", bg="#FFF8D6", font="Arial 10 bold")
lbl_timer = tk.Label(top_right_frame, text=" ", font="Arial")
lbl_timer.grid(row=0, column=0, padx=3, pady=5)
lbl_game_round.grid(row=1, column=0, padx=3, pady=5)
top_right_frame.pack(side=tk.RIGHT, padx=(10, 10))

middle_frame = tk.Frame(window_main, bg="#FFF8D6")
middle_frame.pack(pady=20)

lbl_line = tk.Label(middle_frame, text="____________________________________________________", fg="black")
lbl_line.pack(pady=(0, 5))

lbl_line = tk.Label(middle_frame, text="CHOOSE", fg="green", font=("Arial", 12, "bold"), bg="#FFF8D6")
lbl_line.pack(pady=(0, 5))

choice_frame = tk.Frame(middle_frame, bg="#FFF8D6")
choice_frame.pack()

rock_img = PhotoImage(file="rock.png")
paper_img = PhotoImage(file="paper.png")
scissors_img = PhotoImage(file="scissors.png")

btn_rock = tk.Button(choice_frame, image=rock_img, command=lambda: send_choice("rock"), state=tk.DISABLED)
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(choice_frame, image=paper_img, command=lambda: send_choice("paper"), state=tk.DISABLED)
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(choice_frame, image=scissors_img, command=lambda: send_choice("scissors"), state=tk.DISABLED)
btn_scissors.grid(row=0, column=2, padx=10)

result_frame = tk.Frame(middle_frame, bg="#FFF8D6")
result_frame.pack(pady=(20, 0))

lbl_result = tk.Label(result_frame, text="", font=("Arial", 16), fg="black", bg="#FFF8D6")
lbl_result.pack()

score_frame = tk.Frame(middle_frame, bg="#FFF8D6")
score_frame.pack(pady=(20, 0))

lbl_your_score = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12), fg="black", bg="#FFF8D6")
lbl_your_score.grid(row=0, column=0, padx=10)

lbl_opponent_score = tk.Label(score_frame, text="Opponent Score: 0", font=("Arial", 12), fg="black", bg="#FFF8D6")
lbl_opponent_score.grid(row=0, column=1, padx=10)

bottom_frame = tk.Frame(window_main, bg="#FFF8D6")
bottom_frame.pack(pady=(20, 0))

lbl_line = tk.Label(bottom_frame, text="____________________________________________________", fg="black")
lbl_line.pack(pady=(0, 5))

lbl_line = tk.Label(bottom_frame, text="GAME STATUS", fg="green", font=("Arial", 12, "bold"), bg="#FFF8D6")
lbl_line.pack(pady=(0, 5))

game_status = tk.Text(bottom_frame, height=4, width=40)
game_status.pack()

btn_quit = tk.Button(bottom_frame, text="Quit", font=("Arial", 10), fg="white", bg="red", command=lambda: quit_game())
btn_quit.pack(pady=(10, 0))

def connect():
    global your_name, client
    your_name = ent_name.get()
    if your_name != "":
        window_main.title("Game Client - " + your_name)
        lbl_your_name.config(text="Your name: " + your_name)
        ent_name.delete(0, tk.END)
        btn_connect.config(state=tk.DISABLED)
        btn_disconnect.config(state=tk.NORMAL)
        btn_rock.config(state=tk.NORMAL)
        btn_paper.config(state=tk.NORMAL)
        btn_scissors.config(state=tk.NORMAL)
        client = GameClient(your_name)
        client.connect()

def disconnect():
    global client
    client.disconnect()
    lbl_your_name.config(text="Your name: ")
    lbl_opponent_name.config(text="Opponent name: ")
    lbl_opponent_choice.config(text="Opponent choice: ")
    lbl_timer.config(text="Timer: ")
    lbl_game_round.config(text="Game round: ")
    lbl_result.config(text="")
    lbl_your_score.config(text="Your Score: 0")
    lbl_opponent_score.config(text="Opponent Score: 0")
    game_status.delete("1.0", tk.END)
    btn_connect.config(state=tk.NORMAL)
    btn_disconnect.config(state=tk.DISABLED)
    btn_rock.config(state=tk.DISABLED)
    btn_paper.config(state=tk.DISABLED)
    btn_scissors.config(state=tk.DISABLED)

btn_connect = tk.Button(top_left_frame, text="Connect", font=("Arial", 12), fg="white", bg="green", command=lambda: connect())
btn_connect.pack(padx=5, pady=(5, 10))

btn_disconnect = tk.Button(top_left_frame, text="Disconnect", font=("Arial", 12), fg="white", bg="red", state=tk.DISABLED, command=lambda: disconnect())
btn_disconnect.pack(padx=5, pady=(0, 10))

window_main.mainloop()
