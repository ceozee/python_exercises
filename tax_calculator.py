def tax_calculator(amount, tax):
    print(f'tax value is {round(amount * (tax / 100), 2)}')


amount = input('Enter amount: ')
tax = input('Enter tax percentage: ')

try:
    tax_calculator(int(amount), int(tax))
except ValueError:
    print('Error: Please enter numbers only')