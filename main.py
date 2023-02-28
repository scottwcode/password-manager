# password-manager
# Allows the user to enter usernames and generate random passwords for different
# sites they use and store them in a local file for them to reference or use
#
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generate_pw():
    """ Generate a random password and put it in the pw_input text entry box """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    pw_list = pw_letters + pw_symbols + pw_numbers
    shuffle(pw_list)

    # pw = ""
    # for char in pw_list:
    #     pw += char
    pw = "".join(pw_list)
    pw_input.insert(0, pw)
    # Save pw to clipboard for the user to use it as part of their login
    pyperclip.copy(pw)


def save():
    """ Validate and save results to a file"""
    website = website_input.get()
    username = username_input.get()
    pw = pw_input.get()

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(
            "Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered for {website}:\nUsername: {username}\nPassword: {pw}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {pw}\n")
                website_input.delete(0, END)
                username_input.delete(0, END)
                pw_input.delete(0, END)


# Window frame setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create canvas similar in size to the image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels and Text fields
# Row 1 - Website label and input
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.insert(0, "Amazon")
website_input.focus()

# Row 2 - Username label and input
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "example@gmail.com")

# Row 3 - Password label and input
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)
pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)

# Row 4 - Add buttons
generate_pw_button = Button(text="Generate Passwd", command=generate_pw)
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35,
                    command=save)
add_button.grid(row=4, column=1,  columnspan=2)

window.mainloop()
