personal_information = ['Age', 'Profession', 'Married']

class Customer:
    def _init_(self):
        self.customer = {}
        self.customer_information = {}
        self.create_user()

    def create_user(self):
        self.name = str(input("Full Name: "))
        self.address = input("Address: ")
        self.customer['Name'] = self.name
        self.customer['Address'] = self.address
        print("Tell us about yourself")
        for info in personal_information:
            user_selection = input(f'{info}: ')
            self.customer_information[info] = user_selection
            self.customer['Information'] = self.customer_information
