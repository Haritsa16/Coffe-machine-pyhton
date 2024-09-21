MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
on = True
while on:
    input_coffee = input("What would you like? (Espresso/Latte/Capuccino) ").lower()

    if input_coffee == "espresso" or input_coffee == "latte" or  input_coffee == "capuccino":

        if resources["water"] < MENU[input_coffee]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        if resources["milk"] < MENU[input_coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        if resources["coffee"] < MENU[input_coffee]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
        if all(resources[ingredient] >= MENU[input_coffee]["ingredients"][ingredient] for ingredient in ["water", "milk", "coffee"]):
            print("Please insert coins here!")

            input_quarters = int(input("How many quarters? "))
            input_dimes = int(input("How many dimes? "))
            input_nickles = int(input("How many nickles? "))
            input_pennies = int(input("How many pennies? "))

            total_coins = 0.25*input_quarters + 0.10*input_dimes + 0.05*input_nickles + 0.01*input_pennies

            chosen_cost = float(MENU[input_coffee]['cost'])

            if total_coins < chosen_cost:
                print("Sorry! your coins is not enough")

            if total_coins >= chosen_cost:
                changes = total_coins - chosen_cost
                print(f"Here is ${changes} in change")
                print(f"Here is your {input_coffee}. Enjoy!")

                resources["water"] -= MENU[input_coffee]["ingredients"]["water"]
                resources["milk"] -= MENU[input_coffee]["ingredients"]["milk"]
                resources["coffee"] -= MENU[input_coffee]["ingredients"]["coffee"]
                money += chosen_cost

    if input_coffee == "report":
        print(f"water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]}\nmoney: {money}")

    if input_coffee == "off":
        on = False
