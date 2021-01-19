from RentalSystem import RentalSystem
from Booking import Booking
from Car import Car
from Customer import Customer
import datetime
import unittest


class TestRentalSystem(unittest.TestCase):
    def test_show_car_list(self):   # This method tests the show_car_list method.
        rental_system = RentalSystem()
        self.assertEqual(rental_system.show_car_list('su'), True)
        self.assertEqual(rental_system.show_car_list('se'), True)
        self.assertEqual(rental_system.show_car_list('h'), True)
        self.assertEqual(rental_system.show_car_list('a'), False) # Wrong input given by the user, so the expected
                                                                  # output is False.

    def test_choose_car_group(self):    # This method tests the choose_car_group method.
        rental_system = RentalSystem()
        self.assertEqual(rental_system.choose_car_group(), True)

    def test_user_choice(self):     # This method tests the user_choice method.
        rental_system = RentalSystem()
        self.assertEqual(rental_system.user_choice(), True)

    def test_return_vehicle(self):
        rental_system = RentalSystem()
        self.assertIsNotNone(rental_system, 'the object is not nil')
        customer = rental_system.return_vehicle()
        self.assertIsNotNone(customer, 'The customer object is not none')
        self.assertEqual(customer.customer_id, '100', 'Please enter the customer id for General Customer = 100')


if __name__ == '__main__':
    unittest.main()


class TestBooking(unittest.TestCase):
    def test_valid_booking_date(self):
        car = Car('Alto', 300, True, 'Edin', 'hatchback')
        customer = Customer('100', 'general', 'Elon Musk', 'Nelson Street, London')
        booking_system = Booking(customer, car.car_id, car.price)
        self.assertIsNotNone(booking_system.valid_booking_date(datetime.date.today()))

    def test_book_vehicle(self):
        car = Car('Alto', 300, True, 'Edin', 'hatchback')
        customer = Customer('100', 'general', 'Elon Musk', 'Nelson Street, London')
        booking_system = Booking(customer, car.car_id, car.price)
        self.assertEqual(booking_system.book_vehicle(), True)
        self.assertEqual(booking_system.book_vehicle(), False)


if __name__ == '__main__':
    unittest.main()

