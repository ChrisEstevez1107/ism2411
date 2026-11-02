# Self-Assesment Questions:
# 1. When the order total is 350, the code checks to see which braket it falls within, then it determines which discounts that order qualifies for. It then checks to see if it gets the region bonus and then give the final total and if it will need to go through review.
# 2. id total > 100 and total < 500 checks to see if both conditions are ture at the exact same time, not checking to see if one is true and then the next.
# 3. When checking out on amazon, if I have more than 25$ in my cart I get free shipping, and sometimes I can get more discounts if I select to have a longer delivery time.
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0


 # discount = 0  # replace with correct logic
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")

# Exercise 2:
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")


# Exercise 3:

region = "South" # S is capitalized

if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")
else:
    extra_discount = 0


final = total * (1 - (discount + extra_discount))
print(f"Final: ${final:.2f}")

# Exercise 4:
customer_type = "wholesale"
if region == "South" and total >= 100 and customer_type == "wholesale":
    extra_discount = 0.03

# Exercise 5:
amount = 10000

if amount <= 0:
    print("SUSPICIOS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")

# Exercise 6:

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False # boolean variable

vip_upgrade = True
if total_spent_this_year > 2000 or orders_this_year > 5 and not has_outstanding_balance:
    vip_upgrade = True
else:
    vip_upgrade = False