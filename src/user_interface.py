import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dictionary to store user information
user_data = {}

def show_signup():
    notebook.select(signup_frame)

def show_login():
    notebook.select(login_frame)

def login():
    username = login_entry1.get()
    password = login_entry2.get()

    if username in user_data and user_data[username]["password"] == password:
        print("Login successful")
        show_main_menu()
    else:
        messagebox.showerror("Error", "Login information not found.")

def create_account():
    username = signup_entry1.get()
    password = signup_entry2.get()
    address = signup_entry3.get()
    zipcode = signup_entry4.get()
    city = signup_entry5.get()
    state = signup_entry6.get()
    email = signup_entry7.get()
    phone = signup_entry8.get()

    user_data[username] = {
        "password": password,
        "address": address,
        "zipcode": zipcode,
        "city": city,
        "state": state,
        "email": email,
        "phone": phone
    }

    with open("user_info.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}, Address: {address}, Zipcode: {zipcode}, City: {city}, State: {state}, Email: {email}, Phone: {phone}\n")
    print("Account Created!")
    show_main_menu()

def show_main_menu():
    # Implement your main menu elements here
    pass

root = tk.Tk()
root.title("Package2Go")

notebook = tk.ttk.Notebook(root)

# Sign Up Page
signup_frame = tk.Frame(notebook)

tk.Label(signup_frame, text="Username:").pack()
signup_entry1 = tk.Entry(signup_frame)
signup_entry1.pack()

tk.Label(signup_frame, text="Password:").pack()
signup_entry2 = tk.Entry(signup_frame, show="*")
signup_entry2.pack()

tk.Label(signup_frame, text="Address:").pack()
signup_entry3 = tk.Entry(signup_frame)
signup_entry3.pack()

tk.Label(signup_frame, text="Zipcode:").pack()
signup_entry4 = tk.Entry(signup_frame)
signup_entry4.pack()

tk.Label(signup_frame, text="City:").pack()
signup_entry5 = tk.Entry(signup_frame)
signup_entry5.pack()

tk.Label(signup_frame, text="State:").pack()
signup_entry6 = tk.Entry(signup_frame)
signup_entry6.pack()

tk.Label(signup_frame, text="Email:").pack()
signup_entry7 = tk.Entry(signup_frame)
signup_entry7.pack()

tk.Label(signup_frame, text="Phone:").pack()
signup_entry8 = tk.Entry(signup_frame)
signup_entry8.pack()

signup_button = tk.Button(signup_frame, text="Sign Up", command=create_account)
signup_button.pack()

notebook.add(signup_frame, text='Sign Up')

# Login Page
login_frame = tk.Frame(notebook)

tk.Label(login_frame, text="Username:").pack()
login_entry1 = tk.Entry(login_frame)
login_entry1.pack()

tk.Label(login_frame, text="Password:").pack()
login_entry2 = tk.Entry(login_frame, show="*")
login_entry2.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

notebook.add(login_frame, text='Login')

notebook.pack()

show_login()  # Initially show the Login page

root.mainloop()
