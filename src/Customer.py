class Customer:
    def __init__(self, username, password, address, zipcode, city, state, phone_number, email):
        self.__username = username
        self.__password = password
        self.__adress = address
        self.__zipcode = zipcode
        self.__city = city
        self.__state = state
        self.__phone_number = phone_number
        self.__email = email

    
    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_zipcode(self):
        return self.__zipcode
    
    def __eq__(self, o):
        if isinstance(o, str):
            return self.__email == o
        
        elif isinstance(o, Customer):
            return self.__email == o.__email
        
        return False