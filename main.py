# 1. Завдання: Система управління банком
# import csv
# import os.path
#
# class Customer:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return f"Customer: {self.name}, Balance: {self.balance}"
# class Bank:
#     def __init__(self, filename="customers.csv"):
#         self.filename = filename
#         self.customers = []
#         self.load_customers()  # Виклик методу для завантаження клієнтів з файлу
#
#     def load_customers(self):
#         try:
#             with open(self.filename, 'r') as f:
#                 reader = csv.reader(f)
#                 for row in reader:
#                     name, balance = row
#                     customer = Customer(name, balance)
#                     self.customers.append(customer)
#                 print(f"Customers loaded from {self.filename}.")
#
#         except FileNotFoundError:
#             print(f"File not found by name: {self.filename}")
#
#     def add_customer(self, newCustomerName, newCustomerBalance):
#         customer = Customer(newCustomerName, newCustomerBalance)
#         self.customers.append(customer)
#         self.save_customers()  # Збереження клієнтів після додавання нового
#
#     def save_customers(self):
#         try:
#             with open(self.filename, 'w', newline='') as f:
#                 writer = csv.writer(f)
#                 for customer in self.customers:
#                     writer.writerow([customer.name, customer.balance])
#                 print(f"Customers saved to {self.filename}.")
#
#         except FileNotFoundError:
#             print(f"File not found by name: {self.filename}")
#     def add_customer(self, newCustomerName, newCustomerBalance):
#         customer = Customer(newCustomerName, newCustomerBalance)
#         self.customers.append(customer)
#         self.save_customers()
#
#     def show_customer(self):
#         for index, customer in enumerate(self.customers, start=1):
#             print(f"{index}.{customer.name}")
#
#     def import_customer(self, import_filename):
#         try:
#             with open(import_filename, 'r') as f:
#                 reader = csv.reader(f)
#                 for row in reader:
#                     name, balance = row
#                     customer = Customer(name, balance)
#                     self.customers.append(customer)
#                 self.save_customers()
#                 print(f"Customer from {import_filename} imported correctly.")
#
#         except FileNotFoundError:
#             print(f"File not found by name: {import_filename}")
#
#     def export_customer(self, export_filename):
#         try:
#             with open(export_filename, 'w', newline='') as f:
#                 writer = csv.writer(f)
#                 for customer in self.customers:
#                     writer.writerow([customer.name, customer.balance])
#                 print(f"Customer exported in {export_filename} correctly.")
#
#         except FileNotFoundError:
#             print(f"File not found by name: {export_filename}")
#
#
#     def menu(self):
#         while True:
#             print('''
#             1. Add new Customer.
#             2. Search for Customer.
#             3. Save the data into the file.
#             4. Export data from the file.
#             5. Exit
#             ''')
#             customerChoice = int(input("Make your choice please: "))
#             if customerChoice == 1:
#                 newCustomerName = input("Enter name: ")
#                 newCustomerBalance = int(input("Enter Balance"))
#                 self.add_customer(newCustomerName, newCustomerBalance)
#             elif customerChoice == 2:
#                 self.show_customer()
#             elif customerChoice == 3:
#                 import_filename = os.path.normpath(input("Enter path to .csv file: "))
#                 self.import_customer(import_filename)
#             elif customerChoice == 4:
#                 export_filename = os.path.normpath(input("Enter path to .csv file you want to save your data: "))
#                 self.export_customer(export_filename)
#                 self.export_customer(export_filename)
#             elif customerChoice == 5:
#                 break
#             else:
#                 print("Unknown, please enter again: ")
#
#
# bank = Bank()
# bank.add_customer("Sam", 25)
# bank.show_customer()


# 2. Завдання: Система управління портфелем криптовалют

# class Briefcase:
#     def __init__(self, name):
#         self.name = name
#         self.cryptocurrency = {}
#         self.quotation = {}
#
#     def add_cryptocurrency(self, currency, amount):
#         if currency not in self.cryptocurrency:
#             self.cryptocurrency[currency] = amount
#             print("Currency was successfully saved!")
#         else:
#             self.cryptocurrency[currency] += amount
#
#     def del_cryptocurrency(self, currency):
#         if currency not in self.cryptocurrency:
#             raise ValueError("Currency not found!")
#         else:
#             del self.cryptocurrency[currency]
#     def counter_dollar_values(self):
#         pass
#
#     def show_briefcase(self):
#         self.counter_dollar_values()
#         print(f"Briefcase of the Customer: {self.name}")
#         for currency, amount in self.cryptocurrency.items():
#             dollar_value = self.quotation.get(currency) * amount
#             print(f"Currency: {currency}: Amount: {amount}, Dollar Value: {dollar_value}")
#
# class Dollar_Value:
#     def __get__(self, instance, owner):
#         quotation = instance.quotation.get(instance.currency)
#         amount = instance.cryptocurrency.get(instance.currency)
#         return quotation * amount
#
#
# briefcase = Briefcase("Sam")
# briefcase.quotation = {"GRS": 45, "BTS": 690}
# briefcase.add_cryptocurrency("GRS", 7)
# briefcase.show_briefcase()


# 3. Завдання: Симулятор банкомата з реєстрацією

# class Customer:
#     def __init__(self, name, pin_code, balance):
#         self.name = name
#         self.pin_code = pin_code
#         self.balance = balance
#
#     def correct_pin_code(self, entered_pin_code):
#         if len(self.pin_code) != 4:
#             print("Wrong password. Should be 4 numbers")
#         else:
#             return self.pin_code == entered_pin_code
#
#
#     def show_balance(self):
#         print(f"Your Balance: {self.balance}")
#
#
#     def withdraw_money(self, amount_to_withdraw):
#         if amount_to_withdraw > 0 and self.balance >= amount_to_withdraw:
#             self.balance -= amount_to_withdraw
#             return True
#         return False
#
#
# class ATM:
#     def __init__(self, ATM_balance):
#         self.ATM_balance = ATM_balance
#         self.clients = {}
#
#     def register_new_client(self, name, pin_code, balance):
#         if name not in self.clients:
#             client = Customer(name, pin_code, balance)
#             self.clients[name] = client
#             return client
#         return None
#
#     def enter_to_the_system(self, name, pin_code):
#         if name in self.clients:
#             client = self.clients[name]
#             if client.correct_pin_code(pin_code):
#                 return client
#
#     def show_balance(self):
#         return self.ATM_balance
#
#
# def menu():
#     customer_choice = input("Make your choice:\n1. Registration\n2. Enter\n3. Exit")
#     return customer_choice
#
#
# def customer_choice_menu(client):
#     while True:
#         customer_choice = int(input("Make your choice:\n1. Check Balance\n2. Withdraw Money\n3. Exit"))
#         if customer_choice == 1:
#             balance = client.show_balance()
#             print(f"Your balance is {balance}")
#         elif customer_choice == 2:
#             amount_to_withdraw = float(input("Enter amount you want to withdraw: "))
#             successfull_withdraw = client.withdraw_money(amount_to_withdraw)
#             if successfull_withdraw:
#                 print("Operation Done")
#             else:
#                 print("Not enough money.")
#         elif customer_choice == 3:
#             break
#
#
# if __name__ == "__main__":
#     atm = ATM(10000)
#
#     while True:
#         choice = menu()
#
#         if choice == '1':
#             name = input("Enter your name: ")
#             pin_code = input("Enter your PIN code: ")
#             balance = float(input("Enter your initial balance: "))
#             client = atm.register_new_client(name, pin_code, balance)
#             if client:
#                 print("Registration successful.")
#             else:
#                 print("Client with this name already exists.")
#         elif choice == '2':
#             name = input("Enter your name: ")
#             pin_code = input("Enter your PIN code: ")
#             client = atm.enter_to_the_system(name, pin_code)
#             if client:
#                 customer_choice_menu(client)
#             else:
#                 print("Wrong name or PIN code.")
#         elif choice == '3':
#             break
#         else:
#             print("Invalid choice. Please try again.")














