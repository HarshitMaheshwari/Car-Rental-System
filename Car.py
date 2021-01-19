import random


# This class contains attributes of the car.
class Car:
    def __init__(self, model: object, price: object, is_available: object, assigned_customer: object,
                 group_id: object) -> object:
        self.model = model
        self.price = price
        self.is_available = is_available
        self.assigned_customer = assigned_customer
        self.group_id = group_id

        x = random.randrange(0, 999)    # This generates random car numbers every time. It is used to give more
                                        # realistic feel to the system.
        car_id = ("car{x}".format(x=x))
        self.car_id = car_id

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)



