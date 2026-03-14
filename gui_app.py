import tkinter as tk
from tkinter import messagebox
from storage import save_contacts, load_contacts


def start_contact_manager(window, username):

    contacts_file = f"contacts_{username}.txt"

    contacts = []

    load_contacts(contacts, contacts_file)

    window.title(f"Contact Manager - {username}")
    window.geometry("400x400")


    def refresh_contacts():

        contact_list.delete(0, tk.END)

        contacts.sort(key=lambda c: c["name"].lower())

        for contact in contacts:
            contact_list.insert(tk.END, contact["name"] + " - " + contact["phone"])


    def gui_add_contact():

        name = name_entry.get().strip()
        phone = phone_entry.get().strip()

        if name == "" or phone == "":
            messagebox.showwarning("Input Error", "Enter name and phone")
            return

        contacts.append({"name": name, "phone": phone})

        save_contacts(contacts, contacts_file)

        refresh_contacts()

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)


    def delete_contact():

        selected = contact_list.curselection()

        if not selected:
            return

        index = selected[0]

        contacts.pop(index)

        save_contacts(contacts, contacts_file)

        refresh_contacts()


    def search_contact():

        keyword = search_entry.get().lower()

        contact_list.delete(0, tk.END)

        for contact in contacts:
            if keyword in contact["name"].lower():
                contact_list.insert(tk.END, contact["name"] + " - " + contact["phone"])


    def edit_contact():

        selected = contact_list.curselection()

        if not selected:
            return

        index = selected[0]

        contact = contacts[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])

        contacts.pop(index)

        save_contacts(contacts, contacts_file)

        refresh_contacts()


    tk.Label(window, text="Name").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    tk.Label(window, text="Phone").grid(row=1, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=1, column=1)

    tk.Button(window, text="Add", command=gui_add_contact).grid(row=2, column=0)
    tk.Button(window, text="Delete", command=delete_contact).grid(row=2, column=1)
    tk.Button(window, text="Edit", command=edit_contact).grid(row=2, column=2)

    tk.Label(window, text="Search").grid(row=3, column=0)
    search_entry = tk.Entry(window)
    search_entry.grid(row=3, column=1)

    tk.Button(window, text="Search", command=search_contact).grid(row=3, column=2)
    tk.Button(window, text="Show All", command=refresh_contacts).grid(row=3, column=3)

    contact_list = tk.Listbox(window, width=40, height=10)
    contact_list.grid(row=4, column=0, columnspan=4, pady=10)

    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=4, column=4, sticky="ns")

    contact_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=contact_list.yview)

    refresh_contacts()