#define the menu of the restaurant
menu ={
    'Pizza':50,
    'pasta':40,
    'Burger': 60,
    'coffe': 150,
}

#greet
print("Welcome to BuzzCaf")
print("Pizza: Rs50\npasta: Rs40\nBurger: Rs60\ncoffee: Rs120")

order_total = 0
#70+80=130
item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item{item_1} is not available yet!")

another_order = input("Do you want to add another item?(Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered Item {item_2} is not available!")

print(f"The total amount of items to pay {order_total}")

