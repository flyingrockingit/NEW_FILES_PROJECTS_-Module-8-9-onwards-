import tkinter as tk
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk

def open_image_window():
    messagebox.showinfo("Opening Image", "Loading image in a new window")

    top = Toplevel(root)
    top.title("Image Window")

    img = Image.open("images.jpeg")  
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(top, image=photo)
    img_label.photo = photo  
    img_label.pack(pady=20)

    tk.Button(top, text="Close", command=top.destroy).pack()

root = tk.Tk()
root.title("Main Window Gallery")

tk.Label(root, text="Main Window Gallery", font=("Times New Roman", 16)).pack(pady=10)  
tk.Button(root, text="Open Image", command=open_image_window).pack(pady=20)

root.mainloop()
