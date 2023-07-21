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

moneyAfterPurchase = 0.0


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f'Money: ${round(moneyAfterPurchase, 2)} ')
    return


def money(cost, coffeeType):
    global moneyAfterPurchase
    global resources
    print("Please insert coin")
    quarter = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    userMoney = (quarter * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    #print("user money =", userMoney)
    remainder = userMoney - cost
    #print("remainder = ", remainder)
    if remainder >= 0:
        print(f"Here is ${round(remainder, 2)} in change")
        print(f"Here is your {coffeeType}. Enjoy!")
        moneyAfterPurchase += userMoney
        resources["water"] -= MENU[coffeeType]["ingredients"]["water"]
        resources["milk"] -= MENU[coffeeType]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffeeType]["ingredients"]["coffee"]
    else:
        print("Sorry there is not enough money. Money refunded.")
    return


def checkIngredients(typeCoffee):
    global resources
    global MENU
    if resources["water"] < MENU[typeCoffee]["ingredients"]["water"]:
        return "water"
    if resources["coffee"] < MENU[typeCoffee]["ingredients"]["coffee"]:
        return "coffee"

    if typeCoffee != "espresso":
        if resources["milk"] < MENU[typeCoffee]["ingredients"]["milk"]:
            return "milk"

turn = True
# TODO: 1.print description
while turn:
    question = input("What would you like? (espresso/latte/cappuccino):")

    if question == "report":
        report()
    elif question == "latte":
        if checkIngredients(question) == "water" or checkIngredients(question) == "milk" or checkIngredients(question) == "coffee":
            print(f"Sorry there is not enough {checkIngredients(question)}.")
        else:
            money(MENU["latte"]["cost"], "latte")
    elif question == "espresso":
        money(MENU["espresso"]["cost"], "espresso")
    elif question == "cappuccino":
        money(MENU["cappuccino"]["cost"], "cappuccino")
    elif question == "off":
        turn = False
    else:
        print("Wrong Input")
    print("")
