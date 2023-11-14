import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dictionary to store user information
user_data = {}

# Function to switch to the signup frame
def show_signup():
    notebook.select(signup_frame)

# Function to switch to the login frame
def show_login():
    notebook.select(login_frame)

# Function to validate login information
def login():
    username = login_entry1.get()
    password = login_entry2.get()

    if username in user_data and user_data[username]["password"] == password:
        print("Login successful")
        show_main_menu()
    else:
        messagebox.showerror("Error", "Login information not found.")

# Function to create a new user account
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

    # Write user data to a file
    with open("user_info.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}, Address: {address}, Zipcode: {zipcode}, City: {city}, State: {state}, Email: {email}, Phone: {phone}\n")
    print("Account Created!")
    show_main_menu()

# Placeholder for the main menu
def show_main_menu():
    # Implement your main menu elements here
    pass

# Create the main Tkinter window
root = tk.Tk()
root.title("Package2Go")

# Create a Notebook widget for managing different frames (tabs)
notebook = ttk.Notebook(root)

# Sign Up Page
signup_frame = tk.Frame(notebook)

# Entry fields and labels for signup information
tk.Label(signup_frame, text="Username:").pack()
signup_entry1 = tk.Entry(signup_frame)
signup_entry1.pack()

tk.Label(signup_frame, text="Password:").pack()
signup_entry2 = tk.Entry(signup_frame, show="*")  # Mask password entry
signup_entry2.pack()

# Additional signup information fields
tk.Label(signup_frame, text="Address:").pack()
signup_entry3 = tk.Entry(signup_frame)
signup_entry3.pack()

# ... Additional fields for zip code, city, state, email, phone

# Button to trigger account creation
signup_button = tk.Button(signup_frame, text="Sign Up", command=create_account)
signup_button.pack()

# Add the signup frame to the Notebook
notebook.add(signup_frame, text='Sign Up')

# Login Page
login_frame = tk.Frame(notebook)

# Entry fields and labels for login information
tk.Label(login_frame, text="Username:").pack()
login_entry1 = tk.Entry(login_frame)
login_entry1.pack()

tk.Label(login_frame, text="Password:").pack()
login_entry2 = tk.Entry(login_frame, show="*")  # Mask password entry
login_entry2.pack()

# Button to trigger login validation
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

# Add the login frame to the Notebook
notebook.add(login_frame, text='Login')

# Pack the Notebook widget into the main window
notebook.pack()

show_login()  # Initially show the Login page

root.mainloop()  # Start the GUI event loop
