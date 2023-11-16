import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox
from Customer import Customer
from CustomerDatabase import CustomerDatabase

# Dictionary to store user information
customer = None

path_ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data/user_database.txt'))
db = CustomerDatabase(path_)

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

    if db.user_in_database(username) and db.verify_password(username, password):
        print("Login successful")
        customer = Customer(customer_dict=db.get_user(username))
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
    
    '''zipcode = None
    city = None
    state = None
    email = None
    phone = None'''

    if not db.user_in_database(username):
        id = db.create_user(username, password, address, zipcode, city, state, phone, email)
        customer = Customer(username, password, address, zipcode, city, state, phone, email, id)
        print("Account Created!")
        show_main_menu()
    
    else:
        print("Invalid Information")

# Placeholder for the main menu
def show_main_menu():
    # Destroy the current frame and create the main menu frame
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome to the Main Menu").pack()
    # Add your main menu elements here

    tk.Button(root, text="Make An Order", command=None).pack()
    tk.Button(root, text="Check Order", command=check_order).pack()
    tk.Button(root, text="Account Details", command=None).pack()

def make_order():
    # Destroy the current frame and create the main menu frame
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Make an Order").pack()
    # Add your main menu elements here

def check_order():
    # Destroy the current frame and create the main menu frame
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Check Order").pack()
    # Add your main menu elements here
    tk.Button(root, text="Check Order Details", command=None).pack()
    tk.Button(root, text="Cancel Order", command=None).pack()
    tk.Button(root, text="Status of Order", command=None).pack()

def account_details():
    # Destroy the current frame and create the main menu frame
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Account Details").pack()
    # Add your main menu elements here


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
