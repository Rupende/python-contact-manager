import tkinter as tk
from tkinter import messagebox
from auth import register_user, login_user
from gui_app import start_contact_manager

root = tk.Tk()
root.withdraw()


def login():

    username = username_entry.get()
    password = password_entry.get()

    if login_user(username, password):

        login_window.destroy()

        root.deiconify()

        start_contact_manager(root, username)

    else:

        messagebox.showerror("Login Failed", "Invalid username or password")


def register():

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Enter username and password")
        return

    success = register_user(username, password)

    if success:
        messagebox.showinfo("Success", "User registered successfully")
    else:
        messagebox.showerror("Error", "User already exists")


login_window = tk.Toplevel(root)

login_window.title("Login")
login_window.geometry("300x250")

tk.Label(login_window, text="Contact Manager Login").pack(pady=10)

tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=5)
tk.Button(login_window, text="Register", command=register).pack(pady=5)

login_window.mainloop()