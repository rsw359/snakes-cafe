print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**                                  **')
print('** To quit at any time, type "quit" **')
print('**************************************')

appetizers_list = ["Wings", "Cookies", "Spring Rolls"]
entrees_list = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
deserts_list = ['Ice Cream ', 'Cake', 'Pie']
drink_list = ['Coffee', 'Tea', 'Unicorn Tears']

print("""Appetizers
----------""")

for dish in appetizers_list:
    print(dish)

print('\n')
print("""Entrees
----------""")
for dish in entrees_list:
    print(dish)

print('\n')
print("""Desserts
----------""")
for dish in deserts_list:
    print(dish)

print('\n')
print("""Drinks
----------""")
for dish in drink_list:
    print(dish)

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

items = {}

while True:
    order = input('> ').capitalize()
    order_plural = 'orders'
    order_singular = 'order'
    have_plural = 'have'
    have_singular = 'has'
    if order == 'quit':
        break
    elif order not in items:
        items[order] = 0
    items[order] += 1
    if items[order] > 1:
        order_plural = order_plural
        have_plural = have_plural
    else:
        order_plural = order_singular
        have_plural = have_singular

    print(f'** {items[order]} {order_plural} of  {order} {have_plural} been added to your meal **')
