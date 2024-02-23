from customer_management import Customer
import pandas as pd

all_customers = []
user = Customer()
new_user = True
data = ''

information = ['First Name', 'Last Name', 'Age', 'Profession']


while new_user:
    reset = input('Would you like to create a new user?: ').lower()
    if reset == 'yes':
        user.user_input(*information)
        all_customers.append(user.user_dict)
        data = pd.DataFrame(all_customers)
    else:
        new_user = False
    data.to_csv('Users.csv')
