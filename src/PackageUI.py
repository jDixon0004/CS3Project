import tkinter as tk
from tkinter import messagebox
from CustomerPackage import CustomerPackage


class PackageGUI:
    def __init__(self, root):
        self.root = root
        root.title("Package Management System")

        # Add labels and entry widgets for each field
        tk.Label(root, text="Customer ID").grid(row=0)
        tk.Label(root, text="Package ID").grid(row=1)
        # ... Add labels for other fields

        self.customer_id_entry = tk.Entry(root)
        self.package_id_entry = tk.Entry(root)
        # ... Create entry widgets for other fields

        self.customer_id_entry.grid(row=0, column=1)
        self.package_id_entry.grid(row=1, column=1)
        # ... Place other entry widgets

        # Add buttons
        tk.Button(root, text="Create Package", command=self.create_package).grid(row=6, column=0)
        # ... Add other buttons for update status, etc.

    def create_package(self):
        # Retrieve data from entry widgets
        customer_id = self.customer_id_entry.get()
        package_id = self.package_id_entry.get()
        # ... Retrieve other fields

        # Create an instance of CustomerPackage
        package = CustomerPackage(customer_id, package_id, recipient_name, recipient_address)
        # ... Handle the package as needed

        messagebox.showinfo("Package Created", f"Package {package_id} created for customer {customer_id}")

# Create the main window and pass it to the PackageGUI class
root = tk.Tk()
app = PackageGUI(root)
root.mainloop()
