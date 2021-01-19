import datetime
import Customer


class Booking:

    def __init__(self, customer: Customer, car_id, price):
        self.customer = customer
        self.car_id = car_id
        self.price = price
        self.booking_start_date = datetime
        self.booking_end_date = datetime
        self.total_price = 0

# This method is used to validate the entered booking date by the user.
    def valid_booking_date(self, min_date):
        try:
            input_date = input('Date (dd/mm/yyyy): ')
            day_start, month_start, year_start = map(int, input_date.split('/'))

            if day_start is not None and month_start is not None and year_start is not None:
                date = datetime.date(year_start, month_start, day_start)
                if date < min_date:
                    print('Please enter a valid date')
                    return self.valid_booking_date(min_date)
                else:
                    return date
            else:
                print('Please enter a valid date')
                return self.valid_booking_date(min_date)

        except ValueError:
            print('Please enter a valid date')
            return self.valid_booking_date(min_date)

# This class contains the information of booking period and calculations of the total cost for that period.
    def book_vehicle(self):
        print('Please enter the booking start date')
        self.booking_start_date = self.valid_booking_date(datetime.date.today())
        print('Please enter the booking end date')
        self.booking_end_date = self.valid_booking_date(self.booking_start_date)
        booking_period = (self.booking_end_date - self.booking_start_date)

        if self.booking_end_date > self.booking_start_date:
            self.total_price = self.price * booking_period.days
            final_decision = input(
                'Hey ' + self.customer.customer_name + ',\nAre you sure that you want to book for the selected '
                                                       'dates?(Press Y to confirm or any key to reject): ')
            if final_decision == 'Y' or final_decision == 'y':
                return True
            else:
                re_entered_choice = self.book_vehicle()
                if re_entered_choice:
                    return True
                else:
                    return False

        else:
            print('Please enter a valid start-date and end-date')
            re_entered_choice = self.book_vehicle()
            if re_entered_choice:
                return True
            else:
                return False
