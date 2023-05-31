import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# Create a frame to display the image
image_frame = tk.Frame(root, width=400, height=400)
image_frame.pack()

# Create a frame to hold the text and image
content_frame = tk.Frame(image_frame)
content_frame.pack(pady=10)

# Create a label to display the text "My Image"
text_label = tk.Label(content_frame, text="My Image", font=("Arial", 18))
text_label.pack()

# Create a label to display the image
image_label = tk.Label(content_frame)
image_label.pack()

# Function to show the image
def show_image(image_path):
    # Load the image
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    # Update the image label
    image_label.configure(image=photo)
    image_label.image = photo

# Function to handle button click
def button_click(image_path):
    # Call the function to show the image
    show_image(image_path)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

for i in range(10):
    button = tk.Button(
        button_frame,
        text=str(i+1),
        command=lambda image_path=f"images/{i+1}.png": button_click(image_path),
        width=10,
        height=2
    )
    button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
