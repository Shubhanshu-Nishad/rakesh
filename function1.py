ram_expenses = [2000,1000,500]
hari_expenses = [3000,5000,2000]

total=0
for item in ram_expenses:
    total=total+item
print("Ram total expenses: ",total)

total=0
for item in hari_expenses:
    total=total+item
print("hari total expenses: ",total)

def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

ram_expenses = [2000,1000,500]
hari_expenses = [3000,5000,2000]

ram_expenses=calculate_total(ram_expenses)
hari_expenses=calculate_total(hari_expenses)

print("ram's total is: ",ram_expenses)
print("hari's total is: ",hari_expenses)


def sum(a,b):
    total=a+b
    return total
n = sum(5,6)
print("Total is: ",n)


