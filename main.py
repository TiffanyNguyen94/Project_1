from ingredients import breads, meats, cheeses, toppings

order = []
print("=" * 40)
print("      CUSTOM SANDWICH BUILDER")
print("=" * 40)

#Bread selection

print("\nChoose your bread:\n")
for number, bread in bread.items():
    print(f"{number}. {bread['name']} - " 
          f"${bread['price']:.2f} - "
          f"{bread['weight']}g"
          )

while True:
    bread_choice = input("\nEnter your choice: ")
    if bread_choice in breads:
        selected_bread = breads[bread_choice]

        order.append({"name": selected_bread["name"],"quantity": 1, "price": selected_bread["price"], "weight": selected_bread["weight"]})
        print(f"\nYou selected: {selected_bread['name']}.")
        break
    else:
        print("Invalid choice. Please try again.")


#Meat selection

print("\n" + "-" * 40)
print("\nChoose your meat:\n")

for number, meat in meats.items():
    print(f"{number}. {meat['name']} - "
          f"${meat['price']:.2f} per slice - "
          f"{meat['weight']}g per slice"
          )

    while True:
        meat_choice = input("\nEnter your choice: ")
        if meat_choice in meats:
            selected_meat = meats[meat_choice]
            break
        else:
            print("Invalid choice. Please try again.")

    while True:
        quantity = input(f"How many slices of {selected_meat['name']} would you like? ")
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 0:
                break
        print("Please enter a whole number.")

meat_price = selected_meat["price"] * quantity
meat_weight = selected_meat["weight"] * quantity

order.append({
    "name": selected_meat["name"],
    "quantity": quantity,
    "price": meat_price,
    "weight": meat_weight
})

print(f"\nAdded {quantity} slice(s) of {selected_meat['name']} "
    f"for ${meat_price:.2f} and {meat_weight}g.")


#Cheese selection

print("\n" + "-" * 40)
print("\nChoose your cheese:\n")

for number, cheese in cheeses.items():
    print(f"{number}. {cheese['name']} - "
          f"${cheese['price']:.2f} per slice - "
          f"{cheese['weight']}g per slice"
          )

while True:
    cheese_choice = input("\nEnter your choice: ")
    if cheese_choice in cheeses:
        selected_cheese = cheeses[cheese_choice]
        break
    else:
        print("Invalid choice. Please try again.")

while True:
    quantity = input(f"How many slices of {selected_cheese['name']} would you like? ")
    if quantity.isdigit():
        quantity = int(quantity)
        if quantity > 0:
            break
    print("Please enter a whole number.")   

    cheese_price = selected_cheese["price"] * quantity
    cheese_weight = selected_cheese["weight"] * quantity
    order.append({
        "name": selected_cheese["name"],
        "quantity": quantity,
        "price": cheese_price,
        "weight": cheese_weight
    })


#Topping selection

print("\n" + "-" * 40)
print("\nChoose your toppings:\n")

for number, topping in toppings.items():
    print(
        f"{number}. {topping['name']} - "
        f"${topping['price']:.2f} - "
        f"{topping['weight']}g"
    )

print("5. Finished adding toppings") 

while True:
    topping_choice = input("\nEnter your choice: ")
    if topping_choice == "5":
        break
    elif topping_choice in toppings:
        selected_topping = toppings[topping_choice]
        order.append({
            "name": selected_topping["name"],
            "quantity": 1,
            "price": selected_topping["price"],
            "weight": selected_topping["weight"]
        })

        print(f"{selected_topping['name']} added. ")
    else:
        print("Invalid choice. Please try again.")


#Calculate total price and weight

total_price = 0
total_weight = 0
for item in order:
    total_price += item["price"]
    total_weight += item["weight"]


#Order summary

print("\n")
print("=" * 40)
print("      ORDER SUMMARY")
print

for item in order:
    if item["quantity"] > 1:
        print(
            f"{item['quantity']} x {item['name']} -"
            f" ${item['price']:.2f}"
            f" - {item['weight']}g"
        )
    else:
        print(
            f"{item['name']} -"
            f" ${item['price']:.2f}"
            f" - {item['weight']}g"
        )

print("-" * 40)
print(f"Total Price: ${total_price:.2f}")
print(f"Total Weight: {total_weight}g")
print("=" * 40)

print("\nThank you for using the Custom Sandwich Builder! Enjoy your meal!")