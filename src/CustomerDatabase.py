from Database import Database
from random import randint
import json
import hashlib

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

        hasher = hashlib.sha256()
        hasher.update(bytes(password, 'utf-8'))

        for user in data['users']:
            if user['username'] == username:
                if user['password'] == hasher.hexdigest():
                    return True
                return False
        
        return False
    
    def get_user(self, username=None, id=None):
        self.file.seek(0)
        data = json.load(self.file)

        for user in data['users']:
            if username is not None and user['username'] == username:
                return user
            elif id is not None and user['id'] == int(id):
                return user
        
        return None
    
    def create_user(self, username, password, address, zipcode, city, state, phone_number, email):
        self.file.seek(0)
        data = json.load(self.file)

        while True:
            temp_id = randint(0, 99999999)
            for user in data['users']:
                if user['id'] == temp_id:
                    continue
            
            id = temp_id
            break
        
        hasher = hashlib.sha256()
        hasher.update(bytes(password, 'utf-8'))
                

        new_user = {
            "username": username,
            "password": hasher.hexdigest(),
            "address": address,
            "zipcode": int(zipcode),
            "city": city,
            "state": state,
            "phone_number": int(phone_number),
            "email": email,
            "id": id
        }

        data['users'].append(new_user)

        self.file.seek(0)
        json.dump(data, self.file, indent=4)
        self.file.flush()

        return id

        

