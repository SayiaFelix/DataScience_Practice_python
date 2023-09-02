import statistics

# Menu items and their prices
menu = {
    1: {"item": "Cheese Pizza", "price": 150},
    2: {"item": "Spinach Pizza", "price": 210},
    3: {"item": "Chicken Pizza", "price": 275},
}

# Display the menu
print("Menu:")
for item_number, item_data in menu.items():
    print(f"{item_number}. {item_data['item']}: ${item_data['price']}")

# Prompt the user to choose an item
while True:
    try:
        item_choice = int(input("Enter the item number you'd like to order: "))
        if item_choice in menu:
            break
        else:
            print("Invalid item number. Please choose a valid item number.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")

# Prompt the user to enter the quantity
while True:
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity > 0:
            break
        else:
            print("Quantity must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid quantity.")

# Calculate the bill
selected_item = menu[item_choice]
total_price = selected_item["price"] * quantity

# Display the bill
print(f"Item ordered: {selected_item['item']}")
print(f"Quantity: {quantity}")
print(f"Total bill: ${total_price}")




stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}


def print_all():
    for stock, price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ", round(avg, 2))


def add():
    s = input("Enter a stock ticker to add: ")
    p = input("Enter price of this stock: ")
    p = float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()


def main():
    op = input("Enter operation (print, add): ")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:", op)


if __name__ == '__main__':
    main()
