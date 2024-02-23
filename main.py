from customer_management import Customer

all_customers = {}


for i in range(2):
    user = Customer()
    user_number = i+1
    all_customers[f'User_{user_number}'] = user.customer