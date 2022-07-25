
def get_info():
    
    hours = int(input("Enter hours worked this week: ")) #Create a function that will input and return total hours and is called inside the loop.
    wage = float(input("Enter your hourly wage: ")) #Create a function that will input and return the hourly rate and is called inside the loop.
    tax = float(input("Enter income tax_rate: ")) #Create a function that will input and return the income tax rate and is called inside the loop.
    return hours, wage, tax

def gross_pay(hours, wage): # Gross pay
    gross = hours * wage
    return gross

def taxed(gross, tax): #Amount in Taxes
    amount_taxed = gross * tax
    return amount_taxed

def net_pay(gross, amount_taxed): # Net Pay
    net = gross - amount_taxed
    return net

name = input("What is your name? Enter 'End' to quit: ")
while name != 'End':
    hours, wage, tax = get_info()
    gross = gross_pay(hours, wage)
    amount_taxed = taxed(gross, tax)
    net = net_pay(gross, amount_taxed)

    print(f'Employee Name: {name}')
    print(f'Hours Wokred this week: {hours} hours')
    print(f'Employee Wage: ${wage} dollars')
    print(f'Tax Rate: {tax}%')
    print(f'Gross Pay:${gross:.2f}')
    print(f'Taxes paid: ${amount_taxed:.2f}')
    print(f'Net Pay: ${net:.2f}')

    name = input("What is your name? Enter 'End' to quit: ")
