class AdminUserInterface:
    def __init__(self, admin_id):
        self.admin_id = admin_id
        self.active_orders = {}

    def assign_package(self, package):
        # Assume package is an instance of CustomerPackage
        self.active_orders[package.package_id] = package
        print(f"Package {package.package_id} assigned to a delivery vehicle.")

    def update_package_status(self, package_id, status):
        if package_id in self.active_orders:
            self.active_orders[package_id].update_status(status)
        else:
            print(f"No package with ID {package_id} found in active orders.")

    def cancel_order(self, package_id):
        if package_id in self.active_orders:
            del self.active_orders[package_id]
            print(f"Order {package_id} has been cancelled.")
        else:
            print(f"No package with ID {package_id} found in active orders.")

    def view_all_active_orders(self):
        for package_id, package in self.active_orders.items():
            details = package.get_order_details()
            print(f"Order ID: {package_id}, Status: {details['status']}")
