from customer_management import Customer
from GUI import CustomerRegistration
import pandas as pd

all_customers = []
#user = Customer()
new_user = True
data = ''

information = ['First Name', 'Last Name', 'Age', 'Profession']
first_page = CustomerRegistration(information)
first_page.run()


