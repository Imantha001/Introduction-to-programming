grosssalary = 0
tax = 0
netsalary = 0

grosssalary = float(input("Please enter your Monthly Gross Salary? Rs. "))

if 1<= grosssalary <=99999:
    tax =grosssalary *0
    
elif 99999 <grosssalary <=150000:
    tax =tax+(grosssalary - 99999) *0.05
    
elif (99999 <grosssalary):
    tax = tax+(50000*0.05)
    
if 150001 <= grosssalary <=250000:
    tax =tax+(grosssalary-150000) *0.1
    
elif (150001 <= grosssalary):
    tax =tax+(100000*0.1)
    
if 250000 <grosssalary:
    tax = tax+(grosssalary - 250000) *0.12
    
netsalary = grosssalary - tax

print("Your Monthly Net Salary is: Rs.",netsalary)

