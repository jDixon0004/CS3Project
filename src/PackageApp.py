import tkinter as tk
import os
from tkinter import messagebox
from AdminUserInterface import AdminUserInterface
from CustomerPackage import CustomerPackage
from CustomerDatabase import CustomerDatabase
from PackageDatabase import PackageDatabase

package_db = PackageDatabase(os.path.join(os.path.dirname(__file__), '..', 'data/package_database.txt'))
customer_db = CustomerDatabase(os.path.join(os.path.dirname(__file__), '..', 'data/user_database.txt'))

class PackageApp:
    def __init__(self, master):
        self.master = master
        master.title('Package Management System')

        # CustomerPackage Input Fields
        tk.Label(master, text='Customer ID').grid(row=0, column=0)
        tk.Label(master, text='Recipient Name').grid(row=1, column=0)
        tk.Label(master, text='Recipient Address').grid(row=2, column=0)
        tk.Label(master, text='Recipient City').grid(row=3, column=0)
        tk.Label(master, text='Recipient State').grid(row=4, column=0)
        tk.Label(master, text='Recipient Zipcode').grid(row=5, column=0)
        tk.Label(master, text='Package Weight').grid(row=6, column=0)

        self.customer_id_entry = tk.Entry(master)
        self.recipient_name_entry = tk.Entry(master)
        self.recipient_address_entry = tk.Entry(master)
        self.recipient_city_entry = tk.Entry(master)
        self.recipient_state_entry = tk.Entry(master)
        self.recipient_zipcode_entry = tk.Entry(master)
        self.package_weight_entry = tk.Entry(master)

        self.customer_id_entry.grid(row=0, column=1)
        self.recipient_name_entry.grid(row=1, column=1)
        self.recipient_address_entry.grid(row=2, column=1)
        self.recipient_city_entry.grid(row=3, column=1)
        self.recipient_state_entry.grid(row=4, column=1)
        self.recipient_zipcode_entry.grid(row=5, column=1)
        self.package_weight_entry.grid(row=6, column=1)

        tk.Button(master, text='Create Package', command=self.create_package).grid(row=7, columnspan=2)

        # AdminUserInterface Functions
        tk.Label(master, text='Package ID for Admin').grid(row=8, column=0)
        self.admin_package_id_entry = tk.Entry(master)
        self.admin_package_id_entry.grid(row=8, column=1)

        tk.Button(master, text='Assign Package', command=self.assign_package).grid(row=9, column=0)
        tk.Button(master, text='Update Package Status', command=self.update_package_status).grid(row=9, column=1)
        tk.Button(master, text='Cancel Order', command=self.cancel_order).grid(row=10, column=0)
        tk.Button(master, text='View All Active Orders', command=self.view_all_active_orders).grid(row=10, column=1)

        self.admin_interface = AdminUserInterface(admin_id="Admin1")

    def create_package(self):
        customer_id = self.customer_id_entry.get()
        recipient_name = self.recipient_name_entry.get()
        recipient_address = self.recipient_address_entry.get()
        recipient_city = self.recipient_city_entry.get()
        recipient_state = self.recipient_state_entry.get()
        recipient_zipcode = self.recipient_zipcode_entry.get()
        package_weight = self.package_weight_entry.get()
        
        if customer_db.get_user(id=customer_id) is not None:
            package_id = package_db.create_package(customer_id, recipient_name, recipient_address, recipient_city, recipient_state, recipient_zipcode, package_weight)
            messagebox.showinfo("Success", "Package Created Successfully")
        else:
            messagebox.showinfo("Failure", "Customer With Given ID Does Not Exist")

        # Optionally store or process new_package as needed

    def assign_package(self):
        package_id = self.admin_package_id_entry.get()
        # Retrieve the package instance by package_id and assign it
        package_dict = package_db.retrieve_package(package_id)
        if package_dict is not None:
            retrieved_package = CustomerPackage(package_dict=package_dict)
            self.admin_interface.assign_package(retrieved_package)
            messagebox.showinfo("Success", "Package Assigned Successfully")
        else:
            messagebox.showinfo("Failure", "Invalid Package ID")

    def update_package_status(self):
        # Similar implementation as assign_package
        pass

    def cancel_order(self):
        # Similar implementation as assign_package
        package_id = self.admin_package_id_entry.get()
        db_response = package_db.update_status(package_id, "Cancelled")
        if db_response:
            messagebox.showinfo("Success", "Order Cancelled Successfully")
        else:
            messagebox.showinfo("Failure", "Invalid Package ID")

    def view_all_active_orders(self):
        # Implement logic to view all active orders
        pass

root = tk.Tk()
app = PackageApp(root)
root.mainloop()
