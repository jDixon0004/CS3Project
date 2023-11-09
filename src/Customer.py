class Customer:
    def __init__(self, name, zip_code, phone_number, email):
        self.__name = name
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__email = email

    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_zip_code(self):
        return self.__zip_code