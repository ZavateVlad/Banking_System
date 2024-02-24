from tkinter import *
import pandas as pd
#from customer_management import Customer




class CustomerRegistration:
    def __init__(self, information):
        #super().__init__()
        self.information = information
        self.window = Tk()
        self.window.title('User Registration')
        self.window.geometry('520x300')
        self.window.config(padx=10, pady=10, bg='white')

        welcome_label = Label(text='Welcome to MyBank!', font=('Arial', 32, 'bold'), bg='white')
        welcome_label.pack()

        canvas = Canvas(self.window, width=275, height=183, bg='white', highlightthickness=0)
        self.photo = PhotoImage(file='bank.png')
        canvas.create_image(130, 75, image=self.photo)
        canvas.pack()

        self.entries = {}
        for info in self.information:
            label = Label(text=f'{info}:', bg='white')
            label.pack()
            entry = Entry()
            entry.pack()
            self.entries[info] = entry

        submit_button = Button(text='Submit', command=self.submit)
        submit_button.pack()

    def submit(self):
        all_customers = []
        user_input = {info: entry.get() for info, entry in self.entries.items()}
        all_customers.append(user_input)
        data = pd.DataFrame(all_customers)
        data.to_csv('Users.csv')

    def run(self):
        self.window.mainloop()
