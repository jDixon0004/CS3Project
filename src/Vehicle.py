class Vehicle:
    def __init__(self, id_number, weight_capacity, packages_in_vehicle, package_queue, delivery_destination):
        self.__id_number = id_number
        self.__weight_capacity = weight_capacity
        self.__packages_in_vehicle = packages_in_vehicle
        self.__package_queue = package_queue
        self.__delivery_destination = delivery_destination
    
    def add_package(self, package):
        '''
        Assign package to this vehicle
        '''
        self.__package_queue.add(package)
    
    def deliver_package(self, package_id):
        '''
        Removes the package associated with the given package_id from the vehicle
        '''
        for package in self.__packages_in_vehicle:
            if package_id == package.get_id():
                self.__packages_in_vehicle.remove(package)
                break
        
        