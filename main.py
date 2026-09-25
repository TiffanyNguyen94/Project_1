from ingredients import breads, meats, cheeses, toppings

order = []


#Bread selection

print("\nChoose your bread:\n")
for number, bread in bread.items():
    print(f"{number}. {bread['name']} - ${bread['price']:.2f} - {bread['weight']}g")

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