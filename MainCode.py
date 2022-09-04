MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0.00,
}

Coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}


def coffee_report():
    """Gives a report on the resources within the coffee machine"""
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
    print("Money:", resources["money"])


def check_resources(coffee):
    """Compares the resources needed for the coffee to the resources within the coffee machine"""
    ingredients = MENU[coffee]["ingredients"]
    # making a list to hold the names of resources that the coffee machine needs
    stock_list = []
    stock = True
    # runs through all the different ingredients and compares them
    for x in ingredients:
        if ingredients[x] > resources[x]:
            stock_list.append(x)
            stock = False
    if stock is not True:
        # makes a nicer looking sentence
        stock_up = (" and ".join(stock_list))
        print(f"Sorry there is not enough {stock_up}.")
        stock_list = []
        return False
    else:
        return True


def coin_calculation(coffee, pennies, nickles, dimes, quarters):
    """Calculates whether the user entered enough money, then calculates the change if there is"""
    # sums all the coin vales up to one float type value
    total_money = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    total_cost = MENU[coffee]["cost"]
    # calculates the users change
    user_change = total_money - total_cost
    # checks to see if the user inserted enough coins to pay for the drink
    if user_change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Your change is ${user_change}")
        return True


def update_resources(coffee):
    """reduces the ingredients held within resources and increases the money"""
    ingredients = MENU[coffee]["ingredients"]
    # runs through all the ingredients that are in the coffee machine in order and replaces their values with new ones
    for x in ingredients:
        resources[x] = resources[x] - ingredients[x]
    cost = MENU[coffee]["cost"]
    resources["money"] = resources["money"] + cost


# condition to power off the coffee machine
power = True

# to allow continuous use of the coffee machine
while power is True:

    # condition for while loop
    type_of_coffee = False

    # while loop to continue asking about what coffee the user wants
    while type_of_coffee is not True:

        # Inputs the coffee that the user asks for or a report for the coffee machine owner
        coffee_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")

        # asking for a report
        if coffee_choice == "report":
            coffee_report()
        # everything else is for the coffee
        elif coffee_choice == "espresso":
            type_of_coffee = check_resources("espresso")
        elif coffee_choice == "latte":
            type_of_coffee = check_resources("latte")
        elif coffee_choice == "cappuccino":
            type_of_coffee = check_resources("cappuccino")
        # when users enter  invalid inputs
        else:
            print("INVALID COFFEE TYPE!")

    # reassigning flag back to false
    enough_money = False

    while enough_money is not True:
        user_quarters = float(input("Number of quarters: "))
        user_dimes = float(input("Number of dimes: "))
        user_nickles = float(input("Number of nickles: "))
        user_pennies = float(input("Number of pennies: "))
        enough_money = coin_calculation(coffee_choice, user_pennies, user_nickles, user_dimes, user_quarters)

    # ensure that at the end of the transaction the resources are updated including money
    update_resources(coffee_choice)

    # confirmation that the coffee was received
    print(f"Here is your {coffee_choice}. Enjoy!")

    # providing a power off feature
    power_off = input("Would you like to power off the Coffee Machine?(Y/N): ").lower()
    if power_off == 'y':
        power = False
    elif power_off == 'n':
        power = True
    # if not proper answer was typed then it will assume to power off
    else:
        power = False

# TODO: 1. print a report of all coffee machine resources

# TODO: 2. check to see if the resources in the machine are sufficient to make the requested drink

# TODO: 3. ensure the value of each coin is understood by the program

# TODO: 4. check whether the coins inputted are enough to purchase the coffee

# TODO: 5. proceed to making the coffee and update resources

# TODO: 6. create an "off" button for the coffee machine
