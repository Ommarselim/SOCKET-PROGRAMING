import tkinter as tk

def left_half_window(window):
    window_height = window.winfo_screenheight()
    window_width = window.winfo_screenwidth() // 2

    x = 0
    y = 0

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def right_half_window(window):
    window_height = window.winfo_screenheight()
    window_width = window.winfo_screenwidth() // 2

    x = window.winfo_screenwidth() // 2
    y = 0

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the Tkinter window
window = tk.Tk()

# Set the window title
window.title("Right Half Window")

# Call the right_half_window function to position the window on the right half of the screen
right_half_window(window)

# Start the Tkinter event loop
window.mainloop()
