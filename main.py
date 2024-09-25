from tabulate import tabulate
from math import sqrt

class Membership:
    # Class-level attribute
    data = {'Sumbul': 'Platinum', 'Ana': 'Gold', 'Cahya': 'Platinum'}    
    
    # Initialize attribute
    def __init__(self, username):
        self.username = username  # Instance attribute
        
    # Method to display membership benefits
    def show_benefit(self):
        benefit = [
                    ['Platinum', '15%', 'Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%'],
                    ['Gold', '10%', 'Benefit Silver + Voucher Ojek Online'],
                    ['Silver', '8%', 'Voucher Makanan']
        ]

        benefit_table = tabulate(
                        benefit, 
                        headers=['Membership', 'Discount', 'Another Benefits'], 
                        tablefmt='fancy_grid',
                        stralign='center')

        print(benefit_table)

    # Method to display membership requirements
    def show_requirements(self):
        requirements = [
                        ['Platinum', 8, 15],
                        ['Gold', 6, 10],
                        ['Silver', 5, 7]
        ]

        requirements_table = tabulate(
                            requirements, 
                            headers=['Membership', 'Monthly Expense (juta)', 'Monthly Income (juta)'], 
                            tablefmt='fancy_grid',
                            numalign='right',
                            stralign='center'
        )

        print(requirements_table)
        
    # Method to predict membership using Euclidean distance
    def predict_membership(self, monthly_expense, monthly_income):
        requirements = {
            'Platinum': [8, 15],
            'Gold': [6, 10],
            'Silver': [5, 7]
        }

        # Initialize the minimum distance, corresponding membership variable, and calculation result dictionary
        min_distance = float('inf')
        min_membership = None
        result = {}

        for membership, [member_expense, member_income] in requirements.items():
            # Calculate Euclidean distance
            euclidean_distance = round(sqrt((monthly_expense - member_expense)**2 + (monthly_income - member_income)**2), 2)
            result.update({membership: euclidean_distance})

            if euclidean_distance < min_distance:
                min_distance = euclidean_distance
                min_membership = membership
        
        print(f'Predicted Euclidean distances for {self.username} are {result}')

        # Update the data
        self.data.update({self.username: min_membership})
    
    # Method to display the membership from the database
    def show_membership(self):
        if self.username in self.data: 
            print(f'{self.username} is a {self.data[self.username]} member')
        else:
            print(f'{self.username} is not a member yet')

    # Method to calculate the final price based on membership
    def calculate_price(self, price_list):
        total_price = sum(price_list)

        match self.data[self.username]:
            case 'Platinum':
                final_price = total_price - (total_price * 0.15)
                print(f'{self.username} final price is Rp {final_price:,}')
            case 'Gold':
                final_price = total_price - (total_price * 0.10)
                print(f'{self.username} final price is Rp {final_price:,}')
            case 'Silver':
                final_price = total_price - (total_price * 0.08)
                print(f'{self.username} final price is Rp {final_price:,}')