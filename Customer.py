# This class contains all the attributes of a Customer.
class Customer():
    def __init__(self, customer_id, customer_category, customer_name, customer_address):
        self.customer_id = customer_id
        self.customer_category = customer_category
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.booking_details = 'None'


# This class is inherited from the Customer class. It is made for the VIP/Premium customers where the prices are
# different from a normal customer.
class VipCustomer(Customer):
    def __init__(self, loyalty_card, loyalty_offer):
        self.loyalty_card = loyalty_card
        self.loyalty_offer = loyalty_offer
