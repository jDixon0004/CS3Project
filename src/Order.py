class Order:
    def __init__(self, customer, packages, destination):
        self.__customer = customer
        self.__packages = packages
        self.__destination = destination
        self.__status = 0
        '''
        Status:
            0 = Order Placed
            1 = Out for Delivery
            2 = Delivered
        '''
    
    def update_status(self, status):
        self.__status = status