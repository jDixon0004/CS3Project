class Customer:
    def __init__(self, username=None, address=None, zipcode=None, city=None, state=None, phone_number=None, email=None, id=None, customer_dict=None):
        if customer_dict is not None:
            self.__username = customer_dict['username']
            self.__address = customer_dict['address']
            self.__zipcode = customer_dict['zipcode']
            self.__city = customer_dict['city']
            self.__state = customer_dict['state']
            self.__phone_number = customer_dict['phone_number']
            self.__email = customer_dict['email']
            self.__id = customer_dict['id']
        else:
            self.__username = username
            self.__address = address
            self.__zipcode = zipcode
            self.__city = city
            self.__state = state
            self.__phone_number = phone_number
            self.__email = email
            self.__id = id

    
    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_zipcode(self):
        return self.__zipcode
    
    def get_address(self):
        return self.__address
    
    def get_city(self):
        return self.__city
    
    def get_state(self):
        return self.__state
    
    def get_id(self):
        return self.__id
    
    def __eq__(self, o):
        if isinstance(o, str):
            return self.__email == o
        
        elif isinstance(o, int):
            return self.__id == o
        
        elif isinstance(o, Customer):
            return self.__id == o.__id or self.__email == o.__email
        
        return False
    
