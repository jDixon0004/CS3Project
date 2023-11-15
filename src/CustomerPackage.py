class CustomerPackage:
    def __init__(self, customer_id, package_id, recipient_name, recipient_address, status='Order Received'):
        self.customer_id = customer_id
        self.package_id = package_id
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        self.status = status

    def update_order_details(self, new_name, new_address):
        self.recipient_name = new_name
        self.recipient_address = new_address
        print(f"Order {self.package_id} updated with new details.")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Status for order {self.package_id} updated to {self.status}.")

    def get_order_details(self):
        return {
            'customer_id': self.customer_id,
            'package_id': self.package_id,
            'recipient_name': self.recipient_name,
            'recipient_address': self.recipient_address,
            'status': self.status
        }
