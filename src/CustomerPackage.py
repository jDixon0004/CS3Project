class CustomerPackage:
    def __init__(self, customer_id=None, package_id=None, recipient_name=None, recipient_address=None, status='Order Received', package_dict=None):
        if package_dict is not None:
            self.customer_id = package_dict['customer_id']
            self.package_id = package_dict['package_id']
            self.recipient_name = package_dict['recipient_name']
            self.recipient_address = package_dict['recipient_address']
            self.status = package_dict['status']
        
        else:
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
