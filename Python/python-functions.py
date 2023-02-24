# 1
""" bill = 175.00

tax_rate = 15

total_tax = (bill * tax_rate) /100.00

print('Total tax', total_tax) """

#2


def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) /100

# without print does not return value

print(calculate_tax(175.00, 15))
print(calculate_tax(164.33, 22))