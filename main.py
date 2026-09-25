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
