from Database import Database
from random import randint
import json

class PackageDatabase(Database):
    def __init__(self, pathname):
        super().__init__(pathname)
    
    def create_package(self, customer_id, recipient_name, recipient_address, recipient_city, recipient_state, recipient_zipcode, weight, status='Order Recieved'):
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
            "recipient_city": recipient_city,
            "recipient_state": recipient_state,
            "recipient_zipcode": int(recipient_zipcode),
            "weight": float(weight),
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
        # ***CAUTION*** Messes up format of JSON file (adds extra brackets at the end), so those must be deleted manually 
        self.file.seek(0)
        data = json.load(self.file)

        worked = False

        for i in range(len(data['packages'])):
            if data['packages'][i]['package_id'] == int(package_id):
                data['packages'][i]['status'] = new_status
                worked = True
        
        self.file.seek(0)
        json.dump(data, self.file, indent=4)
        self.file.flush()
        
        return worked