# 1. The accumulator  pattern is essentially a way to store data as a loop runs and gathers data. It lets you carry one piece of data to the next and then gather more infromation and then carry to the next then print it all out at the end.
# 2. There is a great length in the output than there is in the for loop. For loops automatically move through the list whereas the while loop requires you to manually move through the list. The for loop is also more readable and easier to understand than the while loop.
# 3. If you were looking to hire people and had an online intrest form it could first gather their information, then ask what position and their background and education then age and if they arnt within the age range then you still have their information incase they do have good credentials and would like to meet with them another time.

#Exercise 1:
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
for sale in sales:
    total += sale   # update
print(f"Total: ${total}")

total = 0 
count = 0
for sale in sales:
    count += 1

#Exercise 2:
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

#Exercise 3:
current_max = 0 # initialize
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

#Exercise 4:
count_over_100 = 0 # initialize
total_over_100 = 0 # initialize
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

#Exercise 5:
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale<= 100:
        continue
    print(f"${sale}")

#Exercise 6: I would use the for loop because the while loop can end up causing an infinte loop which would make the code useless.

#Exercise 7: 
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount) 
    print(f"${sale}")
    print(f"{discount*100:.0f}% discount")
    print(f"${discounted_price:.2f}")