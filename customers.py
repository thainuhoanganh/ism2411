'''
1. Use bracket notation (dict[key]) when the key is strictly required and its absence indicates
corrupted or invalid data where the program should fail fast. Use .get(key, default) when the
key is optional or may be missing, allowing the program to safely fall back to a sensible default.

2. This pattern directly mirrors a Pivot Table (or SUMIF) in Excel, grouping by a categorical field
and summing values. Python is more scalable for massive datasets because it processes records
in an automated, memory-efficient streaming loop without the UI overhead, file size limits,
or manual refresh steps required by Excel.
'''

print('--- Exercise 1 ---')
customer = {
    'name': 'Alice', # Key:Value
    'email':'alice@gmail.com',
    'tier': 'gold',
    'ytd_spend': 12400, 
}

print(customer['name'])
print(customer['email'])
print(customer ['tier'])
print(customer['ytd_spend'])
print (customer)

print('--- Exercise 2 ---')
customer['phone'] = '555-5555' # adding a new key_value pair to the dictionary
print(customer)

customer ['tier'] = 'platinum'# updating a value of an existing key 
print(customer)

del customer['email'] #deleting a key-value pair 
print(customer)



print('--- Exercise 3 ----')
print(customer.get('email', 'no email on file'))

try:
    print(customer['email'])
except KeyError as error:
    print('KeyError caught:', error)

print('--- Exercsie 4 ---')
for key,value in customer.items():
    print(f'{key}: {value}')
# Iterating without .items() only yields the keys by default, 
# requiring manual indexing (customer[key]) to retrieve corresponding values. 

for key in customer:
    print(f'{key}: {customer[key]}')


print('--- Exercise 5 ---')
tier_discounts = {
    'bronze': 0,
    'silver': 0.05,
    'gold': 0.1,
    'platinum': 0.15,
}

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1-discount_rate)

print(f"Tier:{customer['tier']}")
print(f'Discount Rate: {discount_rate * 100}%')
print(f'Final Price: ${final_price:.2f}')