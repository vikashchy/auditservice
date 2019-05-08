import uuid
import consume_msg as msg
""" This module controls the customer profile , billing & activation """


class Customer:
    def __init__(self,name,country,amount_due,is_active=False):
        self.customer_id = uuid.uuid4()
        self.customer_name = name
        self.country = country
        self.amount_due = amount_due
        if is_active is None:
            self.is_active = True
        else:
            self.is_active = False

    def activate_cust(self):
        self.is_active = True

    def deactivate_cust(self):
        self.is_active = False

    def bill_cust(self,amount):
        self.amount_due += amount


if __name__ == '__main__':
    cust1 = Customer(name='Vikash',country='India',amount_due=100,is_active=True)
    msg.get_messages()
    msg.message