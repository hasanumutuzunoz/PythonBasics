print("Welcome to MyWay Sandwich. Our sandwich is $5")
print("Here are the sandwich toppings: \n Onions, Lettuce' Tomato, Olives, Peppers, Tomatoes")
toppingList = [x for x in input("Please choose 3 toppings separated by space: ").split()]
if len(toppingList) != 3:
    while len(toppingList) != 3:
        toppingList = [x for x in input("Sorry, you can choose ONLY 3 toppings: ").split()]


no = int(input("How many sandwiches would you like to purchase?"))
total = no * 5

print("Your toppings are: ", toppingList)
print("Total Bill : ", total, "dollars")