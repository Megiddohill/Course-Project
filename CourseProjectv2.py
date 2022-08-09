def get_name():
    name = input("What is your name? Enter 'End' to quit: ")
    return name

def get_dates():
    fromdate = input("Enter start date- mm/dd/yyyy: ")
    todate = input("Enter end date- mm/dd/yyyy: ")
    return fromdate, todate

def get_hours():
    hours = int(input("Enter hours worked this week: "))
    return hours

def get_wage():
    wage = float(input("Enter your hourly wage: ")) 
    return wage

def get_tax():
    tax = float(input("Enter income tax_rate: ")) 
    return tax

def gross_pay(hours, wage): 
    gross = float(hours * wage)
    return gross

def taxed(gross, tax): 
    amount_taxed = gross * tax
    return amount_taxed

def net_pay(gross, amount_taxed): 
    net = gross - amount_taxed
    return net

def print_data(empl_info): #prints employee data
    tot_emp = 0
    tot_hours = 0.00
    tot_gross = 0.00
    tot_taxed = 0.00
    tot_net = 0.00
    for empl_list in empl_info: #creates an indexed list
        fromdate = empl_list[0]
        todate = empl_list[1]
        name = empl_list[2]
        hours = empl_list[3]
        wage = empl_list[4]
        tax = empl_list[5]
        gross = gross_pay(hours, wage)
        amount_taxed = taxed(gross, tax)
        net = net_pay(gross, amount_taxed)
        print(fromdate, todate, name, f'{hours:,.2f}', f'{wage:,.2f}', f'{gross:,.2f}', f'{tax:,.2f}', f'{amount_taxed:,.2f}', f'{net:,.2f}')
        tot_emp += 1
        tot_hours += hours
        tot_gross += gross
        tot_taxed += amount_taxed
        tot_net += net
        empl_totals["TotalEmp"] = tot_emp
        empl_totals["TotalHours"] = tot_hours
        empl_totals["TotalGross"] = tot_gross
        empl_totals["TotalTax"] = tot_taxed
        empl_totals["TotalNet"] = tot_net

def print_totals(empl_totals): #function that uses the totals dictionary and assignes value
    print()
    print(f'Total number of employees: {empl_totals["TotalEmp"]}')
    print(f'Total number of hours: {empl_totals["TotalHours"]:,.2f}')
    print(f'Total gross wage: {empl_totals["TotalGross"]:,.2f}')
    print(f'Total taxes deducted: {empl_totals["TotalTax"]:,.2f}')
    print(f'Total net pay: {empl_totals["TotalNet"]:,.2f}')




if __name__ == "__main__":
    
    empl_list = []#creates list
    empl_totals = {}#creates dictionary


    while True:
    
        name = get_name()
        if (name.upper() == "END"):
            break
        fromdate, todate = get_dates()
        hours = get_hours()
        wage = get_wage()
        tax = get_tax()
        empl_info = [fromdate, todate, name, hours, wage, tax]#lsit and index of 0 - 5
        empl_list.append(empl_info) #inserts emp_info into this list
        

print_data(empl_list)
print_totals(empl_totals)
