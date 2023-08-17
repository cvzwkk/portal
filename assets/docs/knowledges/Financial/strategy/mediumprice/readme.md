[Home](/README.md)     

---    

# Medium Price Strategy

Consist in distribute in total amount of orders with increasement per pecentage in every order until desired price.
the script make one olot and one calc of how total amount of money you that have to move until he.

- Example:        
        
Enter your initial capital: 1000000        
Enter total number of coins: 0.01       
Enter the medium price: 29000        
Enter the desired price: 12000      
Enter the number of orders: 7       
Enter the percentage increase in coins between orders: 181        
 
![img](/assets/docs/knowledges/Financial/strategy/mediumprice/IMG/img.png)    

```

import matplotlib.pyplot as plt

def calculate_investment(initial_capital, total_coins, medium_price, desired_price, num_orders, percentage_increase):
    current_price = medium_price
    total_invested = 0
    capital_required = []

    price_range = medium_price - desired_price
    coins_per_order = total_coins / num_orders

    for _ in range(num_orders):
        total_invested += coins_per_order * current_price
        capital_required.append(total_invested)
        coins_per_order *= (1 + percentage_increase / 100)
        current_price -= price_range / (num_orders - 1)

    return capital_required

# Taking user input
initial_capital = float(input("Enter your initial capital: "))
total_coins = float(input("Enter total number of coins: "))
medium_price = float(input("Enter the medium price: "))
desired_price = float(input("Enter the desired price: "))
num_orders = int(input("Enter the number of orders: "))
percentage_increase = float(input("Enter the percentage increase in coins between orders: "))

capital_required = calculate_investment(initial_capital, total_coins, medium_price, desired_price, num_orders, percentage_increase)

# Plotting
plt.plot(capital_required, marker='o')
plt.xlabel('Order')
plt.ylabel('Capital Required')
plt.title('Capital Required per Order')
plt.grid(True)
plt.show()

# Displaying textual output
for i, capital in enumerate(capital_required):
    print(f"Order {i + 1}: Capital Required = {capital:.2f}")

```
---    


- Textual mode:

```

def calculate_investment(initial_capital, total_coins, medium_price, desired_price, num_orders, percentage_increase):
    current_price = medium_price
    total_invested = 0

    price_range = medium_price - desired_price
    coins_per_order = total_coins / num_orders

    for _ in range(num_orders):
        total_invested += coins_per_order * current_price
        print(f"At {current_price:.2f} price, you would need {total_invested:.2f} capital.")
        coins_per_order *= (1 + percentage_increase / 100)
        current_price -= price_range / (num_orders - 1)

# Taking user input
initial_capital = float(input("Enter your initial capital: "))
total_coins = float(input("Enter total number of coins: "))
medium_price = float(input("Enter the medium price: "))
desired_price = float(input("Enter the desired price: "))
num_orders = int(input("Enter the number of orders: "))
percentage_increase = float(input("Enter the percentage increase in coins between orders: "))

calculate_investment(initial_capital, total_coins, medium_price, desired_price, num_orders, percentage_increase)

```
