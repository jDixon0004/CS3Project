from Database import Database
from random import randint
import json

class PackageDatabase(Database):
    def __init__(self, pathname):
        super().__init__(pathname)
    
    def create_package(self, customer_id, recipient_name, recipient_address, status='Order Recieved'):
        self.file.seek(0)
        data = json.load(self.file)

        while True:
            temp_id = randint(0, 99999999)
            for package in data['packages']:
                if package['package_id'] == temp_id:
                    continue
            
            package_id = temp_id
            break
                

        new_package = {
            "customer_id": int(customer_id),
            "package_id": package_id,
            "recipient_name": recipient_name,
            "recipient_address": recipient_address,
            "status": status
        }

        data['packages'].append(new_package)

        self.file.seek(0)
        json.dump(data, self.file, indent=4)
        self.file.flush()

        return package_id
    
    def retrieve_package(self, package_id):
        self.file.seek(0)
        data = json.load(self.file)

        for package in data['packages']:
            if package['package_id'] == int(package_id):
                return package
        
        return None
    
    def update_status(self, package_id, new_status):
        self.file.seek(0)
        data = json.load(self.file)

        worked = False

        for package in data['packages']:
            if package['package_id'] == int(package_id):
                package['status'] = new_status
                worked = True
        
        self.file.flush()
        self.file.seek(0)
        json.dump(data, self.file, indent=4)
        self.file.flush()
        
        return worked