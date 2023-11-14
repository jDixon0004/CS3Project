class Customer:
    def __init__(self, username=None, password=None, address=None, zipcode=None, city=None, state=None, phone_number=None, email=None, customer_dict=None):
        if customer_dict is not None:
            self.__username = customer_dict['username']
            self.__password = customer_dict['password']
            self.__address = customer_dict['address']
            self.__zipcode = customer_dict['zipcode']
            self.__city = customer_dict['city']
            self.__state = customer_dict['state']
            self.__phone_number = customer_dict['phone_number']
            self.__email = customer_dict['email']
        else:
            self.__username = username
            self.__password = password
            self.__address = address
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
    
