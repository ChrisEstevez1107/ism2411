# customers.py
# Author: Christopher Estevez
# Module 11 Lab: Customer Dictionary & Lookup

print("---Exercise 1---")
customer = {
    "name": "Alice", #Key : Value ,
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("\n---Exercise 2---")
customer['phone'] = '555-555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' # Updating the value of an existing key
del customer['Name'] # Deleting a key-value pair from the dictionary
print(customer)