from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denominator Calculator")
root.configure(bg="#ADD8E6")
root.geometry("650x480")

upload = Image.open("1000 AED.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="#ADD8E6")
label.place(x=100, y=180)

label1 = Label(root, text="Welcome to the Future of Technology!", 
               bg="#4682B4", fg="white", font=("Helvetica", 18, "bold"))
label1.place(relx=0.5, y=50, anchor=CENTER)

def msg():
    Msgbox = messagebox.askyesno("Alert", "Do you want to proceed?")
    if Msgbox:  
        topwin()

button1 = Button(root, text="Let's Get Started", bg="#008080", fg="white", 
                 font=("Helvetica", 14, "bold"), padx=10, pady=5, command=msg)
button1.place(relx=0.5, y=100, anchor=CENTER)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="#2E3F6E")
    top.geometry("400x450")

    Label(top, text="Enter Your Total Amount", bg="#1C2D5B", fg="white", 
          font=("Helvetica", 14, "bold"), pady=10).pack(fill=X)

    entry = Entry(top, font=("Helvetica", 14), bd=3, justify=CENTER)
    entry.pack(pady=15)

    Label(top, text="Number of Notes per Denomination", bg="#1C2D5B", fg="white", 
          font=("Helvetica", 12, "bold"), wraplength=350, pady=5).pack(fill=X)

    l1 = Label(top, text="AED 1000", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))
    l2 = Label(top, text="AED 500", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))
    l3 = Label(top, text="AED 100", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))
    l4 = Label(top, text="AED 50", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))
    l5 = Label(top, text="AED 20", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))
    l6 = Label(top, text="AED 10", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))
    l7 = Label(top, text="AED 5", bg="#2E3F6E", fg="#FFD700", font=("Helvetica", 12, "bold"))

    t1 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    t2 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    t3 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    t4 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    t5 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    t6 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)
    t7 = Entry(top, font=("Helvetica", 12), width=5, justify=CENTER, bd=2)

    def calculator():
        try:
            global amount
            amount = int(entry.get())

            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note20 = amount // 20
            amount %= 20
            note10 = amount // 10
            amount %= 10
            note5 = amount // 5

            for t in [t1, t2, t3, t4, t5, t6, t7]:
                t.delete(0, END)

            t1.insert(0, note1000)
            t2.insert(0, note500)
            t3.insert(0, note100)
            t4.insert(0, note50)
            t5.insert(0, note20)
            t6.insert(0, note10)
            t7.insert(0, note5)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")

    btn = Button(top, text="Calculate", command=calculator, bg="#008080", fg="white",
                 font=("Helvetica", 12, "bold"), padx=10, pady=5)
    btn.place(x=150, y=100)

    l1.place(x=50, y=150); t1.place(x=200, y=150)
    l2.place(x=50, y=180); t2.place(x=200, y=180)
    l3.place(x=50, y=210); t3.place(x=200, y=210)
    l4.place(x=50, y=240); t4.place(x=200, y=240)
    l5.place(x=50, y=270); t5.place(x=200, y=270)
    l6.place(x=50, y=300); t6.place(x=200, y=300)
    l7.place(x=50, y=330); t7.place(x=200, y=330)

root.mainloop()
