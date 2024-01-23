from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    passwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = passwd_entry.get()
    credentials = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Ooops", message="Fields website and password are empty. Please choose a website and password.")
    else:
        try:
            with open(file="credentials.json", mode="r") as file:
                new_credentials = json.load(file)
        except FileNotFoundError:
            with open(file="credentials.json", mode="w") as file:
                json.dump(credentials, file, indent=4)
        else:
            new_credentials.update(credentials)
            with open(file="credentials.json", mode="w") as file:
                json.dump(new_credentials, file, indent=4)
        finally:
            website_entry.delete(0, END)
            passwd_entry.delete(0, END)

#----------------------- SEARCH PASSWORD ------------------------------#
def find_password():
    try:
        with open("credentials.json", "r") as file:
            credentials = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found",message="There's no file with credentials")
    else:
        website = website_entry.get()
        if website in credentials:
            messagebox.showinfo(title=f"{website} Credentials", message=f"Email: {credentials[website]['email']}\nPassword: {credentials[website]['password']} ")
            passwd_entry.insert(0, f"{credentials[website]['password']}")
        else:
            messagebox.showinfo(title="Website not found", message=f"There are not credentials for {website}")







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=300, height=300, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=59)
email_entry.insert(0, "test@test.com")
email_entry.grid(column=1, row=2, columnspan=2)

passwd_label = Label(text="Password:")
passwd_label.grid(column=0, row=3)
passwd_entry = Entry(width=40)
passwd_entry.grid(column=1, row=3)

add_button = Button(text="Add", width=37, command=save_data)
add_button.grid(column=1, row=4)

generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(column=2, row=3, columnspan=2)

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()