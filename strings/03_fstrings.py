# string formatting

template = '{}, you are awesome. Take this ${} watch'

person1 = 'Vaidika'
price1 = 10000
person2 = 'Gautam'
price2 = 12000

# using format method
print(template.format(person1, price1))
print(template.format(person2, price2))

# using fstrings
print(f"{person1}, you are awesome. Take this ${price1} bag.")
print(f"{person2}, you are awesome. Take this ${price2} bag.")