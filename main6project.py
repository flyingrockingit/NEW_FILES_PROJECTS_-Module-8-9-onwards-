from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Bank Denomination Calculator")
root.configure(bg="#E0F7FA")
root.geometry("360x640")

canvas = Canvas(root, bg="#E0F7FA")
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

main_frame = Frame(canvas, bg="#E0F7FA")
canvas.create_window((0, 0), window=main_frame, anchor="n")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

main_frame.bind("<Configure>", on_frame_configure)

try:
    img = Image.open("1000 AED.jpg")
    img = img.resize((300, 180))
    photo = ImageTk.PhotoImage(img)
    img_label = Label(main_frame, image=photo, bg="#E0F7FA")
    img_label.pack(pady=10)
except:
    Label(main_frame, text="Bank Denomination Calculator", 
          bg="#00796B", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack(pady=10)

Label(main_frame, text="Enter Total Amount (AED):", bg="#E0F7FA", fg="#004D40",
      font=("Helvetica", 14, "bold")).pack(pady=10)
amount_entry = Entry(main_frame, font=("Helvetica", 14), bd=3, justify=CENTER)
amount_entry.pack(pady=5)

denominations = [1000, 500, 100, 50, 20, 10, 5]
entries = []

for denom in denominations:
    frame = Frame(main_frame, bg="#B2DFDB", pady=5)
    frame.pack(pady=5)

    Label(frame, text=f"AED {denom}", bg="#004D40", fg="white",
          font=("Helvetica", 12, "bold"), width=12).pack(side=LEFT, padx=5)
    ent = Entry(frame, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    ent.pack(side=LEFT, padx=5)
    entries.append(ent)

# Functions
def calculate():
    try:
        amount = int(amount_entry.get())
        if amount < 0:
            raise ValueError
        remaining = amount
        for i, denom in enumerate(denominations):
            count = remaining // denom
            remaining %= denom
            entries[i].delete(0, END)
            entries[i].insert(0, count)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number")

def clear_entries():
    amount_entry.delete(0, END)
    for ent in entries:
        ent.delete(0, END)

button_frame = Frame(main_frame, bg="#E0F7FA", pady=15)
button_frame.pack(pady=10)

calc_btn = Button(button_frame, text="Calculate", command=calculate,
                  bg="#00796B", fg="white", font=("Helvetica", 12, "bold"),
                  width=15, pady=10)  
calc_btn.pack(side=LEFT, padx=10)

clear_btn = Button(button_frame, text="Clear", command=clear_entries,
                   bg="#C62828", fg="white", font=("Helvetica", 12, "bold"),
                   width=15, pady=10)  
clear_btn.pack(side=LEFT, padx=10)  # Changed to LEFT for centering

root.mainloop()
