# While I have already taken a java course and lists are similar, the lists in python make significantly more sense. The list in python are suprisingly easy to naviagate through to find specifc values in the list.
# A time in business where I would use lists is when I am keeping track of inventory. I would use a list to keep track of the items in stock and the quantity of each item. This would allow me to easily see what items are low in stock and need to be reordered.
# Exercise 1
print("- - - Exercise 1: Build a List - - -")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print("- - - Exercise 2: Index Practice - - -")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3
print("- - - Exercise 3: List Slicing - - -")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
print("- - - Exercise 4: List Methods - - -")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
print("- - - Exercise 5: Tuple Comparison - - -")
coords = (40.7128, -74.0060)    

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught:", {error})
    print("Tuples protect coordinates from being changed.")

# Exercise 6
print("- - - Exercise 6: List Average Sales - - -")

sales = [150, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sales: {max(sales)}")
print(f"Worst sales: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sales: {best}")
print(f"Worst sales: {worst}")

# Exercise 7
print("- - - Exercise 7: Accumulator pattern - - -")
prices = [9.99, 14.99, 4.99,24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

# Exercise 8
print("- - - Exercise 8: Filter - - -")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")