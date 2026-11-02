# Exercise #5 Obervations
#When printing ("5" + "3") it returns the string 53. When print (5 + 3) it returns the numeric calculation 8.
#When printing the different types, ("12") print a string, (12) prints a integer, (12.0) prints a float, and (True) prints a boolean.
# 1. "Unknown format code 'f' for object of type 'str'" because you enter a double value, but the program is expecting a string, so it does not understand the numbers you put in.
# 2. In Exercise 5 it returns 53 not 8 because you are adding the two strings together, not doing the arthemetic. You cannot add strings, but you can add integers.
# 3. You could use variables, types, and f-strings in real life to gather data from clients and input it into a spreadsheet. Then the person looking at the data can see an organized list with the data from each person.

# Exercise #1: Variables and types

product = "Notebook"
unit_price = 6.67
quantity = 420
in_stock = True

print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))

# Exercise #2: f-string practice

print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${unit_price * quantity}")

# Exercise #3: Input version

product_in = input("Product Name: ")
price_in = float(input("Unit Price: "))
quantity_in = int(input("Quantity: "))

print(f"{quantity_in} units of {product_in} at ${price_in:.2f} each = ${price_in * quantity_in:.2f}")

# Exercise #4: Multi-variable product card

unit_cost = 6.67
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100

print(f"Product: {product}\nRevenue: ${revenue:.2f}\nCost: ${unit_cost:.2f}\nMargin: {margin:.2f}%")