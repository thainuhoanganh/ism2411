# self-assessment 
# 1. The first bug I spotted was the missing colon in the ' for sale in sales' loop. I found it from the traceback since it threw an immediate SyntaxError. 
# This tells me that my bugging instincts currently rely heavily on Python's error messages for syntax issues, 
# but I need to practice reading the code more carefully to catch logic errors (like `total = sale`) on my own.

# 2. The apply_discount(price, tier) functions takes a price and a membership tier ( like 'gold'). It returns the discounted tier, and a colleague could use it easily
# because the function name and inputs clearly explain what it does. 

# 3. AI Disclosure: I used AI as a debugging partner to identify syntax errors with nested quotes in f-strings, fix a logic error in my discount percentages, and correctly structure my final file. 
# Reflection: The AI built my understanding because it explained *why* my code was breaking (such as the quote conflicts in f-strings 
# and how variable scope works) rather than just giving me the final code, which helped me learn the underlying concepts.

# exercise 1
def calculate_tax(price,rate):
    return price * rate

# calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f'Tax for $100 at 7%: ${tax1:.2f}')
print(f'Tax for $250 at 8%: ${tax2:.2f}')
print(f'Tax for $350 at 5%: ${calculate_tax(350,0.05):.2f}')


# exercise 2
# defining a function with multiple parameters
def apply_discount(price,tier):

    if tier == 'gold':
        return price * 0.85
    elif tier == 'silver':
        return price * 0.90
    elif tier == 'bronze':
        return price * 0.95
    else:
        return price

# calling the fucntion with different tiers
original_price = 200
for tier in ['gold', 'silver', 'bronze', 'none']:
    print(f'{tier}: ${apply_discount(original_price, tier):.2f}')


# exercise 3
def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#calling the final_prce function
print(f'final_price(200,"gold", 0.07) = ${final_price(200,"gold", 0.07):.2f}')

# exercise 4
orders = [(200,'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.07
for price, tier in orders:
    total = final_price(price, tier,rate)
    print(f'Price: ${price} | Tier: {tier} | Total: ${total:.2f}')

# exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# exercise 6 
x = 100 # global x is declared outside 

def double_it():
    x = 999 # local x is declared inside double_it()
    return x * 2

print(x) # prints 100 (uses the global variable x = 100)
print(double_it())# prints 1998 (uses the local variable x = 999 inside the function, then multiplies by 2)
print(x)# prints 100 (no, x has not changed; the global variable remains the same)

# Scope Explanation:
# In Python, "Scope" determines where a variable can be seen and used. 
# In the code above, we actually have two independent 'x' variables despite having the same name
# Calling the function doesn't overwrite the global x, which is why print(x) at the end still prints 100.