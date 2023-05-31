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

window_height = window_main.winfo_screenheight()
window_width = window_main.winfo_screenwidth() // 2

x = window_main.winfo_screenwidth() // 2
y = 0

window_main.geometry(f"{window_width}x{window_height}+{x}+{y}")


window_main.columnconfigure(0,weight=1)
window_main.title("Game Client")