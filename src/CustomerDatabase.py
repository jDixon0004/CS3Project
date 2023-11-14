from Database import Database
import json

class CustomerDatabase(Database):
    def __init__(self, pathname):
        super().__init__(pathname)

    def user_in_database(self, username):
        self.file.seek(0)
        data = json.load(self.file)

        for user in data['users']:
            if user['username'] == username:
                return True
        
        return False
    
    def verify_password(self, username, password):
        self.file.seek(0)
        data = json.load(self.file)

        for user in data['users']:
            if user['username'] == username:
                if user['password'] == password:
                    return True
                return False
        
        return False
    
    def get_user(self, username):
        self.file.seek(0)
        data = json.load(self.file)

        for user in data['users']:
            if user['username'] == username:
                return user
        
        return None
    
    def create_user(self, username, password, address, zipcode, city, state, phone_number, email):
        self.file.seek(0)
        data = json.load(self.file)

        new_user = {
            "username": username,
            "password": password,
            "address": address,
            "zipcode": zipcode,
            "city": city,
            "state": state,
            "phone_number": phone_number,
            "email": email
        }

        data['users'].append(new_user)

        self.file.seek(0)
        json.dump(data, self.file, indent=4)
        self.file.flush()
