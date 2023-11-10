import tkinter as tk

# Dictionary to store user information
user_data = {}

root = tk.Tk()
root.title("Package2Go")

tk.Label(root, text="Username:").pack()  # Creates a label widget
entry1 = tk.Entry(root) # Creates an Entry widget for username input
entry2 = tk.Entry(root) # Creates an Entry widget for password input
entry3 = tk.Entry(root) # Creates an Entry widget for address input
entry4 = tk.Entry(root) # Creates an Entry widget for zipcode input
entry5 = tk.Entry(root) # Creates an Entry widget for city input
entry6 = tk.Entry(root) # Creates an Entry widget for state input
entry7 = tk.Entry(root) # Creates an Entry widget for email input
entry8 = tk.Entry(root) # Creates an Entry widget for phone input

entry1.pack()  # Packs the Entry widget into the tkinter window


def login():
    username = entry1.get()
    password = entry2.get()

    if username in user_data and user_data[username]["password"] == password:
        print("Login successful")
        show_main_menu()
    else:
        print("Login failed. Please try again")

def create_account():
    username = entry1.get()
    password = entry2.get()
    address = entry3.get()
    zipcode = entry4.get()
    city = entry5.get()
    state = entry6.get()
    email = entry7.get()
    phone = entry8.get()

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
    # Destroy the current frame and create the main menu frame
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome to the Main Menu").pack()
    # Add your main menu elements here

root = tk.Tk()
root.title("Package2Go")

# ... (same as before)

# Buttons
signup_button = tk.Button(root, text="Sign Up", command=create_account)
signup_button.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
