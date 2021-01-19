from Car import Car
from Customer import Customer, VipCustomer
from enum import Enum
from Booking import Booking


# Created an enum for the customer category.
class UserType(Enum):
    general = 'general'
    vip = 'vip'


# Created an enum for the vehicle category.
class VehicleType(Enum):
    sedan = 'sedan'
    suv = 'suv'
    hatchback = 'hatchback'


# This class has multiple methods for all the calculations required for the rental_system. It is responsible for
# creating instances like car instance, user instance etc.
class RentalSystem:
    def __init__(self):
        sedan_1 = Car('Audi A4', 160, True, '', VehicleType.sedan.name)
        sedan_2 = Car('Mercedes C220', 200, True, '', VehicleType.sedan.name)
        sedan_3 = Car('Jaguar XF', 150, True, '', VehicleType.sedan.name)
        suv_1 = Car('Audi Q3', 300, True, '', VehicleType.suv.name)
        suv_2 = Car('Ford Ecosport', 280, True, '', VehicleType.suv.name)
        suv_3 = Car('Bmw X1', 340, True, '', VehicleType.suv.name)
        suv_4 = Car('Bmw X5', 450, True, '', VehicleType.suv.name)
        hatchback_1 = Car('swift', 100, True, '', VehicleType.hatchback.name)
        hatchback_2 = Car('alto', 80, True, '', VehicleType.hatchback.name)
        hatchback_3 = Car('civic', 120, True, '', VehicleType.hatchback.name)
        self.sedan = [sedan_1, sedan_2, sedan_3]
        self.suv = [suv_1, suv_2, suv_3, suv_4]
        self.hatchback = [hatchback_1, hatchback_2, hatchback_3]
        self.car_type_input = ''
        self.total_available_cars = 0

        self.customer_vip = VipCustomer(True, 10)
        self.customer_vip.customer_id = 101
        self.customer_vip.customer_name = 'Jeff Bezos'
        self.customer_vip.customer_address = 'Park Street, Bristol'
        self.customer_vip.customer_category = UserType.vip
        self.customer_vip.booking_details = 'None'
        self.customer_general = Customer('100', UserType.general, 'Elon Musk', 'Nelson Street, London')

    # This method is used to fetch the details of all the cars present in a particular group.
    def car_detail_group_wise(self, car):
        if car.is_available:
            self.total_available_cars += 1
            print('Name: ' + str(car.model).upper() + '\n', 'Car ID: ' + str(car.car_id) + '\n',
                  'Price: ' + str(car.price) + '\n', 'Group ID: ' + str(car.group_id) + '\n',
                  'Availability: ' + str(car.is_available) + '\n')

    # This method takes the input from the user to return the available cars list in a particular group.
    def show_car_list(self, car_type_input):
        if car_type_input == 'SE' or car_type_input == "se":  # Shows all the Sedan cars available.
            self.total_available_cars = 0
            print('-------------')
            print('SEDAN GROUP')
            print('-------------')
            for i in self.sedan:
                self.car_detail_group_wise(i)
            return True

        elif car_type_input == 'SU' or car_type_input == "su":  # Shows all the SUV cars available.
            self.total_available_cars = 0
            print('-------------')
            print('SUV GROUP')
            print('-------------')
            for i in self.suv:
                self.car_detail_group_wise(i)
            return True

        elif car_type_input == 'H' or car_type_input == "h":  # Shows all the Hatchback cars available.
            self.total_available_cars = 0
            print('-------------')
            print('HATCHBACK GROUP')
            print('-------------')
            for i in self.hatchback:
                self.car_detail_group_wise(i)
            return True

        else:
            print('Wrong option selected, Please select the correct option \n')
            return False

    # It displays the groups available for the user to choose from.
    def choose_car_group(self):
        print('\nPress H for Hatchback' + '\n' + 'Press SU for SUV' + '\n' + 'Press SE for Sedan')
        self.car_type_input = input('Choose the car type: ')
        result = self.show_car_list(self.car_type_input)
        if result:
            print('Total available cars in this group: ', self.total_available_cars)
            return True
        else:
            recall = self.choose_car_group()
            if recall:
                return True
            else:
                return False

    # This method takes customer id as input and returns the customer object containing the details of the customer
    # to categorise them as VIP customer or a General customer.
    def return_vehicle(self):
        customer_id_input = input('Please enter your Customer Id: ')
        customer: Customer
        if customer_id_input == '101':  # Customer Id for VIP customers.
            customer = self.customer_vip
            return customer
        elif customer_id_input == '100':  # Customer Id for General customers.
            customer = self.customer_general
            return customer
        else:
            print('Invalid Customer Id, Please enter the correct Customer Id')
            valid_customer = self.return_vehicle()
            if valid_customer is not None:
                return True
            else:
                return False

    # This is a check made to validate the input car ID.
    def check_for_wrong_car_id(self):
        print('You have entered wrong Car Id, Please enter the correct Car Id from the above list.')
        re_entered = self.fetch_car_details()
        if re_entered is not None:
            return re_entered
        else:
            return False

    # This method is used to fetch the car details using the car id entered by the user.
    def fetch_car_details(self, car_id=None):
        car_id_selected = car_id
        if car_id_selected is None:
            car_id_selected = input('Please enter the Car Id: ')
            print('\nThank you for selecting ')

        fetched_sedan_car = [car for car in self.sedan if car.car_id == car_id_selected]
        fetched_suv_car = [car for car in self.suv if car.car_id == car_id_selected]
        fetched_hatchback_car = [car for car in self.hatchback if car.car_id == car_id_selected]

        if len(fetched_sedan_car) > 0:
            return fetched_sedan_car[0]
        elif len(fetched_suv_car) > 0:
            return fetched_suv_car[0]
        elif len(fetched_hatchback_car) > 0:
            return fetched_hatchback_car[0]
        else:
            return_car = self.check_for_wrong_car_id()
            return return_car

    # This method takes the input from the user where they want to rent a car or return a previously rented car. If
    # the customer wants to rent a car, then it calls the choose_car_group method to show the list of available groups
    # And if the customer returns a car, then it prints out the booking details fetched from customer object.
    def user_choice(self):
        user_input = input('Enter your choice (N/Y): ')

        if user_input == 'N' or user_input == 'n':  # Input to rent a car.
            result = self.choose_car_group()
            if result:
                return True
            else:
                return False
        elif user_input == 'Y' or user_input == 'y':    # Input to return a previously rented car.
            customer = self.return_vehicle()
            if customer is not None:    # The customer object contains all the booking details.
                booking: Booking = customer.booking_details
                print('Bill Details:\n')
                print('Customer Name: ', booking.customer.customer_name)
                print('Returning Car Id: ', booking.car_id)
                print('Car per day Price: ', booking.price)
                print('Booking start date: ', booking.booking_start_date)
                print('Booking end date: ', booking.booking_end_date)
                print('Total payable amount: ', booking.total_price)

                car_return_input = input('Please pay the amount by entering P or else enter any key to cancel the '
                                         'return\n')
                if car_return_input == 'P' or car_return_input == 'p':
                    car = self.fetch_car_details(car_id=booking.car_id)
                    car.is_available = True
                    customer.booking_details = 'None'
                    self.initialize_system()
                else:
                    self.initialize_system()
            else:
                return False

        else:
            print('Looks like you have selected an invalid choice. Please enter a valid option')
            result = self.user_choice()
            if result:
                return True
            else:
                return False

    # This method contains the calculation of the total number of cars available for rent.
    def calculate_total_available_cars(self):
        total_cars = len([sedan_car for sedan_car in self.sedan if sedan_car.is_available is True]) + \
                     len([suv_car for suv_car in self.suv if suv_car.is_available is True]) + \
                     len([hatchback_car for hatchback_car in self.hatchback if hatchback_car.is_available is True])
        return total_cars

    # This method returns the customer type according to the user input to print out offers available. Eg. Vip
    # customer gets a 10% discount.
    def get_customer_details(self):
        customer_id = input('\nPlease enter your Customer Id: ')
        customer: Customer
        if customer_id == '101':
            customer = self.customer_vip
            print('\nHey ' + customer.customer_name + ' Thank you for being our premium customer \nWe have a surprise '
                                                      'discount for you')
            print('Discount: ' + str(self.customer_vip.loyalty_offer) + '%\n')
            return customer
        elif customer_id == '100':
            customer = self.customer_general
            print('Hey, ' + customer.customer_name + ' you are a general customer. Please visit the store to get the '
                                                     'loyalty card offers')
            return customer
        else:
            print('You have entered an invalid customer Id, Please recheck and enter the correct Id')
            valid_customer = self.get_customer_details()
            if valid_customer is not None:
                return valid_customer
            else:
                return False

    # This method calls essential methods for initializing.
    def initialize_system(self):
        total_available_cars = self.calculate_total_available_cars()
        print('Total available cars: ', total_available_cars)
        print('\nIf you want to rent a car then press N or press Y to return a car')
        user_choice = self.user_choice()
        if user_choice:
            car: Car = self.fetch_car_details()

            print('Car Name:', car.model)
            print('Car Price:', car.price)
            print('Car Id:', car.car_id)

            customer = self.get_customer_details()

            if hasattr(customer, 'booking_details'):
                if customer.booking_details != 'None':
                    print('You have already booked a car, Please return the previous car to rent a new one.')
                    self.initialize_system()

            booking = Booking(customer, car.car_id, car.price)
            is_booked = booking.book_vehicle()
            if is_booked:
                print('initialize billing')
                effective_price = booking.total_price
                if customer.customer_category == UserType.vip:
                    discount_percentage = (effective_price * self.customer_vip.loyalty_offer) / 100
                    effective_price = effective_price - discount_percentage
                print('Total booking amount to be paid: ', effective_price)
                booking.total_price = effective_price
                confirmation_input = input('Press C to confirm or any key to reject the booking: ')
                if confirmation_input == 'C' or confirmation_input == 'c':
                    car.is_available = False
                    customer.booking_details = booking
                    print('\nCongratulations! Your car has been booked.')
                    self.initialize_system()

                else:
                    print('I hope you had a great experience. Please revisit for more updates.')
                    user_reselection = input('Do you want to exit or make changes to your previous selection \nPress '
                                             'R for reselection or any key to exit ')
                    if user_reselection == 'R' or user_reselection == 'r':
                        self.initialize_system()
                    else:
                        print('Thank you for visiting. \U0001f600')

            else:
                print('Thank you for visiting!')
                self.initialize_system()
