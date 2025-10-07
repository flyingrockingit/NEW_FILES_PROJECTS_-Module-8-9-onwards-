import tkinter as tk
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

root = tk.Tk()
root.title("🎮 Guess the Number")
root.geometry("420x360")
root.config(bg="#f0f0f0")

def check_guess():
    global attempts, secret_number
    try:
        guess = int(entry_guess.get())
    except ValueError:
        label_result.config(text="⚠️ Please enter a valid number!", fg="orange")
        return

    attempts += 1
    remaining = max_attempts - attempts

    if guess < secret_number:
        label_result.config(text=f"Too low! {remaining} attempts left.", fg="red")
    elif guess > secret_number:
        label_result.config(text=f"Too high! {remaining} attempts left.", fg="red")
    else:
        label_result.config(text=f"🎉 Correct! You guessed it in {attempts} tries.", fg="green")
        label_hint.config(text="")
        button_guess.config(state="disabled")
        return

    if attempts == 2:
        label_hint.config(text=f"💡 Hint: {'Even' if secret_number % 2 == 0 else 'Odd'}")
    elif attempts == 3:
        label_hint.config(text=f"💡 Hint: {'1-50' if secret_number <= 50 else '51-100'}")
    elif attempts == 4:
        lower = secret_number - 10 if secret_number > 10 else 1
        upper = secret_number + 10 if secret_number < 100 else 100
        label_hint.config(text=f"💡 Hint: Between {lower} and {upper}")

    if attempts >= max_attempts:
        label_result.config(text=f"❌ Out of attempts! The number was {secret_number}.", fg="black")
        button_guess.config(state="disabled")
        label_hint.config(text="")

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    label_result.config(text="Game restarted! Guess again 🎯", fg="blue")
    label_hint.config(text="")
    button_guess.config(state="normal")

# --- Widgets ---
label_title = tk.Label(root, text="Guess the Number 🎯", font=("Arial", 18, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

entry_guess = tk.Entry(root, font=("Arial", 14), justify="center")
entry_guess.pack(pady=5)

button_guess = tk.Button(root, text="Guess", font=("Arial", 16), command=check_guess, bg="#4CAF50", fg="white")
button_guess.pack(pady=5)

label_result = tk.Label(root, text="I'm thinking of a number between 1 and 100.", font=("Arial", 12), bg="#f0f0f0")
label_result.pack(pady=10)

label_hint = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="#f0f0f0", fg="#555")
label_hint.pack(pady=5)

button_restart = tk.Button(root, text="Restart Game", command=restart_game, bg="#008CBA", fg="white", font=("Arial", 12))
button_restart.pack(pady=10)

root.mainloop()
