import tkinter as tk
from tkinter import PhotoImage

from tkinter import messagebox
import socket
from time import sleep
import threading
from tkinter import *
import pygame
from PIL import Image,ImageTk


pygame.mixer.init()

# MAIN GAME WINDOW

window_main = tk.Tk()


window_main.rowconfigure(0,weight=1)
window_main.rowconfigure(1,weight=1)
window_main.rowconfigure(2,weight=1)
window_main.rowconfigure(3,weight=1)
window_main.rowconfigure(4,weight=1)
window_main.rowconfigure(5,weight=1)

window_height = window_main.winfo_screenheight()
window_width = window_main.winfo_screenwidth() // 2

x = window_main.winfo_screenwidth() // 2
y = 0

window_main.geometry(f"{window_width}x{window_height}+{x}+{y}")

window_main.columnconfigure(0,weight=1)
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





img3=Image.open(r"bg.jpg")
img3=img3.resize((window_main.winfo_screenwidth(),window_main.winfo_screenheight()),Image.Resampling.LANCZOS)
photoimg3=ImageTk.PhotoImage(img3)

bg_img=Label(window_main,image=photoimg3)
bg_img.place(x=0,y=0,width=window_main.winfo_screenwidth(),height=window_main.winfo_screenheight())

bg_img.columnconfigure(0,weight=1)

##############################################




top_welcome_frame = tk.Frame(window_main,background="#f9f9f9")
top_welcome_frame.grid(row=0,column=0)
top_welcome_frame.columnconfigure(0,weight=1)
top_welcome_frame.columnconfigure(1,weight=1)



lbl_name = tk.Label(top_welcome_frame, text="Name:",background="#f9f9f9")
lbl_name.grid(row=0,column=0)
ent_name = tk.Entry(top_welcome_frame)
ent_name.grid(row=0,column=1,pady=(5,5),padx=12)
btn_connect = tk.Button(top_welcome_frame, text="Connect",command=lambda: connect(),background="#f48498",padx=30)
btn_connect.grid(row=1,column=0,columnspan=2,pady=20)

top_message_frame = tk.Frame(window_main)
top_message_frame.grid(row=1,column=0)

lbl_welcome = tk.Label(top_message_frame,background="#f9f9f9")
lbl_welcome.grid(row=1,column=0)
image_welcome = tk.Label(top_message_frame,background="#f9f9f9")
image_welcome.grid(row=2,column=0)




top_frame = tk.Frame(window_main,background="#f9f9f9")
top_frame.grid_forget()







# My choice Image 
your_image_frame = tk.LabelFrame(top_frame , text="My choice",width=300 , height=300 ,background="#f9f9f9")
your_image_frame.grid(row=0,rowspan=2,column=1,sticky="news")
your_image_frame.grid_propagate(False)
your_image_label = tk.Label(your_image_frame,background="#acd8aa",width=300 , height=300)
your_image_label.grid(row=0,column=1,sticky="news")
your_image_label.grid_propagate(False)


#Opponent choice image
opponent_image_frame = tk.LabelFrame(top_frame , text="Opponent choice",width=300 , height=300 ,background="#f9f9f9")
opponent_image_frame.grid(row=0,rowspan=2,column=2,sticky="news")
opponent_image_frame.grid_propagate(False)

opponent_image_label = tk.Label(opponent_image_frame,background="#f48498",width=300 , height=300)
opponent_image_label.grid(row=0,column=2,sticky="news")
opponent_image_label.grid_propagate(False)








top_right_frame = tk.Frame(top_frame,background="#f9f9f9")
top_right_frame.grid(row=0,rowspan=2,column=3)

lbl_opponent_name = tk.Label(top_right_frame, text="Opponent name: ", font="Helvetica 13 bold",background="#f9f9f9" )
lbl_opponent_name.grid(row=0, column=0, padx=5, pady=8)

lbl_game_round = tk.Label(
    top_right_frame,
    text="round (x) starts in",
    foreground="black",
    font="Helvetica 14 bold",
    background="#f9f9f9"
)
lbl_timer = tk.Label(
    top_right_frame, text=" ", font="Helvetica 24 bold", foreground="red" ,background="#f9f9f9"
)
lbl_game_round.grid(row=1, column=0, padx=5, pady=5)
lbl_timer.grid(row=2, column=0, padx=5, pady=5)



round_frame = tk.Frame(top_frame,background="#f9f9f9")
round_frame.grid(row=0,column=0,rowspan=2)

lbl_your_name = tk.Label(round_frame, text="Your name: ", font="Helvetica 13 bold",foreground="black",background="#f9f9f9")
lbl_your_name.grid(row=0, column=0, padx=5, pady=8)

lbl_round = tk.Label(round_frame, text="Round",font="Helvetica 15 bold",background="#f9f9f9")
lbl_round.grid(row=1,column=0)

# this label to make the gui look better
help = tk.Label(round_frame, text="",font="Helvetica 15 bold",background="#f9f9f9")
help.grid(row=2,column=0)


lbl_your_choice = tk.Label(top_frame, text="Your choice: " + "None", font="Helvetica 15 bold",background="#f9f9f9")
lbl_your_choice.grid(row=2,column=1)
lbl_opponent_choice = tk.Label(top_frame, text="Opponent choice: " + "None", font="Helvetica 15 bold",background="#f9f9f9")
lbl_opponent_choice.grid(row=2,column=2)
lbl_result = tk.Label(top_frame, text="", foreground="#43b0f9", font="Helvetica 15 bold",background="#f9f9f9")
lbl_result.grid(row=0,column=1,columnspan=2)





lbl_final_result = tk.Label(top_frame, text=" ", font="Helvetica 15 bold", foreground="blue")
lbl_final_result.grid(row=3,column=1,columnspan=2)



button_frame = tk.Frame(window_main)
button_frame.grid(row=4,column=0)


# photo_one = Image.open("images/1.png")
# resized_image = photo_one.resize((int(window_width/5), int(window_width/5)), Image.ANTIALIAS)
# photo_one = ImageTk.PhotoImage(resized_image)

photos = []

for i in range(1, 11):
    # Load the original image
    photo = Image.open(f"images/{i}.png")
    
    # Resize the image
    resized_image = photo.resize((int(window_width/5-5), int(window_width/5-5)), Image.Resampling.LANCZOS)
    
    # Convert the resized image to a format compatible with Tkinter
    photo_tk = ImageTk.PhotoImage(resized_image)
    
    # Store the photo in the list
    photos.append(photo_tk)



# photo_one = PhotoImage(file=r"images/1.png")
# photo_two = PhotoImage(file=r"images/2.png")
# photo_three = PhotoImage(file=r"images/3.png")
# photo_four = PhotoImage(file=r"images/4.png")
# photo_five = PhotoImage(file=r"images/5.png")
# photo_six = PhotoImage(file=r"images/6.png")
# photo_seven = PhotoImage(file=r"images/7.png")
# photo_eight = PhotoImage(file=r"images/8.png")
# photo_nine = PhotoImage(file=r"images/9.png")
# photo_ten = PhotoImage(file=r"images/10.png")





btn_one = tk.Button(
    button_frame,
    text="one",
    command=lambda image=f"images/{1}.png": [choice("1"), show_image(image)],
    state=tk.DISABLED,
    image=photos[0],
    bg="#f94144"
)
btn_one.grid(row=0, column=0)

btn_two = tk.Button(
    button_frame,
    text="two",
    command=lambda image=f"images/{2}.png": [choice("2"), show_image(image)],
    state=tk.DISABLED,
    image=photos[1],
    bg="#f3722c"

)
btn_two.grid(row=0, column=1)

btn_three = tk.Button(
    button_frame,
    text="three",
    command=lambda image=f"images/{3}.png": [choice("3"), show_image(image)],
    state=tk.DISABLED,
    image=photos[2],
    bg="#f8961e"

)
btn_three.grid(row=0, column=2)

btn_four = tk.Button(
    button_frame,
    text="four",
    command=lambda image=f"images/{4}.png": [choice("4"), show_image(image)],
    state=tk.DISABLED,
    image=photos[3],
    bg="#f9844a"

)
btn_four.grid(row=0, column=3)

btn_five = tk.Button(
    button_frame,
    text="five",
    command=lambda image=f"images/{5}.png": [choice("5"), show_image(image)],
    state=tk.DISABLED,
    image=photos[4],
    bg="#f9c74f"

)
btn_five.grid(row=0, column=4)

btn_six = tk.Button(
    button_frame,
    text="six",
    command=lambda image=f"images/{6}.png": [choice("6"), show_image(image)],
    state=tk.DISABLED,
    image=photos[5],
    bg="#90be6d"

)
btn_six.grid(row=1, column=0)

btn_seven = tk.Button(
    button_frame,
    text="seven",
    command=lambda image=f"images/{7}.png": [choice("7"), show_image(image)],
    state=tk.DISABLED,
    image=photos[6],
    bg="#43aa8b"

)
btn_seven.grid(row=1, column=1)

btn_eight = tk.Button(
    button_frame,
    text="eight",
    command=lambda image=f"images/{8}.png": [choice("8"), show_image(image)],
    state=tk.DISABLED,
    image=photos[7],
    bg="#4d908e",
    

)
btn_eight.grid(row=1, column=2)

btn_nine = tk.Button(
    button_frame,
    text="nine",
    command=lambda image=f"images/{9}.png": [choice("9"), show_image(image)],
    state=tk.DISABLED,
    image=photos[8],
    bg="#577590"

)
btn_nine.grid(row=1, column=3)

btn_ten = tk.Button(
    button_frame,
    text="ten",
    command=lambda image=f"images/{10}.png": [choice("10"), show_image(image)],
    state=tk.DISABLED,
    image=photos[9],
    bg="#277da1"

)
btn_ten.grid(row=1, column=4)




def who_win(your_choice, opponent_choice):
    

    total = int(your_choice) + int(opponent_choice)
    print(total)
    if total % 2 == 0:
        return "even" , total
    else:
        return "odd" , total



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





def show_image(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Resize the image to fit the frame
    image = image.resize((300, 300), Image.Resampling.LANCZOS)
    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)
    # Update the image in the frame
    your_image_label.config(image=photo)
    your_image_label.image = photo




def show_o_image(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Resize the image to fit the frame
    image = image.resize((300, 300), Image.Resampling.LANCZOS)
    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)
    # Update the image in the frame
    opponent_image_label.config(image=photo)
    opponent_image_label.image = photo


def connect():
    play_audio_click()
    if len(ent_name.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter your first name <e.g. John>"
        )
    else:
        your_name = ent_name.get()
        lbl_your_name["text"] = "Your name: " + your_name
        connect_to_server(your_name)

def play_audio_win():
    pygame.mixer.Sound("hehe.mp3").play()
def play_audio_click():
    pygame.mixer.Sound("click.wav").play()



def count_down(my_timer, nothing):
    global game_round ,total
    game_round = game_round + 1

    lbl_game_round["text"] = "Game round " + str(game_round) + " starts in"

    while my_timer > 0:
        my_timer = my_timer - 1
        print("game timer is: " + str(my_timer))
        lbl_timer["text"] = my_timer
        sleep(1)

    enable_disable_buttons("enable")
    lbl_round["text"] = "Round - " + str(game_round)
    lbl_final_result["text"] = (
                    " RESULT: "
                    + str(your_score)
                    + " - "
                    + str(opponent_score)
                    + " "
                    
                )


def choice(arg):
    play_audio_click()
    global your_choice, client, game_round
    your_choice = arg
    lbl_your_choice["text"] = "Your choice: " + your_choice
    lbl_your_choice["font"] = "Helvetica 15 bold"

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

        if not from_server:
            break

        if from_server == "even":
            your_type ="EVEN !"
            image = Image.open("even.png")
            image = image.resize((300, 120))
            image_tk = ImageTk.PhotoImage(image)
            image_welcome.configure(image=image_tk,bg="#f9f9f9")
        if from_server == "odd":
            your_type="ODD !"
            image = Image.open("odd.png")
            image = image.resize((300, 120))
            image_tk = ImageTk.PhotoImage(image)
            image_welcome.configure(image=image_tk,bg="#f9f9f9")


        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                lbl_welcome["text"] = (
                    " Welcome " + your_name + "! Waiting for player 2"
                )
            elif from_server == "welcome2":
                lbl_welcome["text"] = (
                    " Welcome " + your_name + "! Game will start soon"
                )
            

        elif from_server.startswith("opponent_name$"):
            opponent_name = from_server.replace("opponent_name$", "")
            lbl_opponent_name["text"] = "Opponent name: " + opponent_name
            top_frame.grid(row=2,column=0)

            # we know two users are connected so game is ready to start
            threading._start_new_thread(count_down, (game_timer, ""))
            top_welcome_frame.grid_forget()
            lbl_welcome.grid_forget()
            
            

        elif from_server.startswith("$opponent_choice"):
            # get the opponent choice from the server
            opponent_choice = from_server.replace("$opponent_choice", "")
            image_path =f"images/{opponent_choice}.png"  
            show_o_image(image_path)




            print(your_choice)
            print(opponent_choice)

            # figure out who wins in this round
            global total
            who_wins , total = who_win(your_choice, opponent_choice)
            round_result = " "
            if who_wins == "even" and your_type =="EVEN !":
                your_score = your_score + total
                round_result = "WIN"
            elif who_wins == "odd" and your_type== "EVEN !":
                opponent_score = opponent_score + total
                round_result = "LOSS"

            elif who_wins == "even" and your_type== "ODD !":
                opponent_score = opponent_score + total
                round_result = "LOSS"
            elif who_wins == "odd" and your_type== "ODD !":
                your_score = your_score + total
                round_result = "WIN"

            # Update GUI
            lbl_opponent_choice["text"] = "Opponent choice: " + opponent_choice
            lbl_result["text"] = "" + round_result
            lbl_opponent_choice["font"] = "Helvetica 15 bold"


            # is this the last round e.g. Round 5?
            if your_score>=50 or opponent_score>=50:
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
                play_audio_win()
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
            if your_score < 50 and opponent_score < 50:
            # Start the timer
                threading._start_new_thread(count_down, (game_timer, ""))

    sck.close()


window_main.mainloop()
