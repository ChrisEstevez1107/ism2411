# Self Assesment Questions:
# 1. The program will produce an incorrect answer, by not dividing by 100 you subtract 1 from some number greater than one resulting in a negative number.
# 2. Another area you would need this is if you are try to fill boxes of paper. You need to know how many sheets can fit in each box and then how many left over you have to fill more boxes.
# 3. I tend to confuse the dividing and modulo a lot and just forget about how the remainder is important. Some more practice on this would help stregthen that gap.
# Revenue, Margins and Discount Calculator

# Exercise 1:
price = 50
quantity = 12
revenue = price * quantity

# ,.2f has two job -> thousands separator and gives us EXACTLY 2 decimal places

print(f"Revenue: ${revenue:,.2f}")

# Exercise 2:

cost = 32
price = 50
margin = (price - cost) / price
print(f"Margin: {margin:.1%}")

# Exercise 3: Boolean Logic
# Product A  wins if margin_a > margin_b
# Product A with Margin 60%, Product B with Margin (80-60)/80 = 25%
margin_a = 0.60
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Exercise 4: Logic Combo

is_premium = price > 100 and margin > 0.3 # Remember to review basic logic operators: and, or, not
price = 150
margin = .35
print(f"Is Premium: {is_premium}")

# Exercise 5: Division + Mod

print(17/3) # 5.666666666667
print(17//3) #

# Exercise 7: 

BOX_SIZE = 24 # ALL UPPER CASE MEANS CONSTANTS
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE # Floor division is not abstrct math
loose_items = items_ordered % BOX_SIZE # Moodulo is not abstract math
exact_fit = loose_items == 0
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

# Exercise 6:

# inputs name, retail_price, cost, quantity_sold, discount_rate

product = input("Enter the product name: ")
retail_price = float(input("Enter the retail price: "))
quantity_sold = int(input("Enter the quantity sold: "))
discount_pct = int(input("Enter the discount percentage: "))
cost = float(input("Enter the cost: "))
print("=" * 50)
revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1 - discount_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

#Output
print(f"Product: {product}")
print(f"Revenue: ${revenue:.2f}")
print(f"Discounted Revenue: ${discounted_revenue:.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")