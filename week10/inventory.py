'''
Reflection 1: 
What suprised me most is how flexible lists are with negative indexing and slicing like [::2],
and how easily they can manipulated without manually tracking sizes. 

Reflection 2: 
When calculating daily sales at coffee shop, doing it in Excel required writing filter formulas across sheets. 
Using a Python list with a loop automates filtering high sales and finding the average instantly. 
'''

#exercise 1: build a list
print ('---Exercise 1: Build a list---')

inventory = ['pen', 'notebook', 'stapler', 'tape', 'marker' ]
print(inventory)
print(len(inventory))

#exercise 2: Index Practice 
print('---Exercise 2: Index Practice---')
print(inventory[0]) #alwasy graps the first item
print(inventory[-1])#alwasy graps the last item

middle = len(inventory) // 2
print (inventory[middle]) #alwasy graps the middle item (not harded code)

#exercise 3: 
print('---Exercise 3: List Slicing---')
print(inventory[:3]) #alwasy graps first three item
print(inventory[-2:])#alwasy graps last two item
print(inventory[::2])

#exercise 4:
print('--- Exercise 4: List Methods ---')

inventory.append('envelope') #add new 
print(inventory)

inventory.remove('tape')#remove it 
print(inventory)

inventory.sort()#sort the list in alphabetical order 
print(inventory)

#exercuse 5: 
print('---Exercise 5: Tuple Comparsion---' )
coords = (40.7128, -74.0060) # NY city coordinates

try: 
    coords[0] = 99
except TypeError as error: 
    print(f' TypeError caught: {error}')
    print (f'Tuples protect coordinates from being changed by accident')

print(coords)

#exercise 6: 
print('--- Exercise 6: List Average Sales ---')
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f'Total sales: {total}')
print(f'Number of sales: {count}')
print(f'Average sales: {average}')
print(f'Best sale: {max(sales)}')
print(f' Worst sale: {min(sales)}')

#exercise 7:
print('--- Exercise 7: Accumulator pattern ---')
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices: 
   discounted.append(round(price * 0.9, 2))# apply a 10% discount

print(prices)
print(discounted)

#exercise 8: 
print('--- Execise 8: Filter ---')
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales: 
    if amount > 300:
        high_sales.append(amount)

print (high_sales)
print(f'Count: {len(high_sales)}')
print(f'Average: {sum(high_sales) / len(high_sales)}')

