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
