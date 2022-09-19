from tkinter import *
from tkinter import messagebox
import os
import random
import sv_ttk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(10, 15)
    nr_numbers = random.randint(1, 3)
    nr_symbols = random.randint(1, 3)

    password = ""

    for letter in range(1, nr_letters + 1):
        password += random.choice(letters)

    for number in range(0, nr_numbers + 1):
        password += random.choice(numbers)

    for symb in range(0, nr_symbols + 1):
        password += random.choice(symbols)

    pwd = list(password)
    random.shuffle(pwd)
    password_entry.delete(0, "end")
    password_entry.insert(0, "".join(pwd))
    password_entry.clipboard_append(password_entry.get())
    save_password_label.config(text="Password copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def open_file():
    with open("password_file.txt", "a") as f:
        f.writelines(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
        f.flush()


def save_credentials():
    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Empty Fields", message="Please fill all the fields!")

    elif messagebox.askyesno(title=website_entry.get(), message=f"Email: {username_entry.get()}\nPassword: {password_entry.get()}\nIs this ok?") is True:
        with open("password_file.txt", "a") as f:
            f.writelines(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.minsize(width=500, height=400)
window.config(padx=50, pady=50)
window.maxsize(width=500, height=400)

photo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=190)
canvas.create_image(100, 95, image=photo)
canvas.grid(column=1, row=0, columnspan=1)

website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:", font=("Arial", 12))
email_username_label.grid(column=0, row=2)

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 12))
password_label.grid(column=0, row=3)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

add_button = Button(text="Save Credentials", command=save_credentials)
add_button.grid(column=1, row=5)
add_button.config(pady=10, padx=10)

save_password_label = Label(text="", font=("Arial", 8))
save_password_label.grid(column=1, row=4)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

sv_ttk.set_theme("dark")

mainloop()