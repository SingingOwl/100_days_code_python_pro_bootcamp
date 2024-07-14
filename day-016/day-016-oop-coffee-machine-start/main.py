from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_module = CoffeeMaker()
coffee_menu = Menu()
coffee_maker_money_module = MoneyMachine()

machine_on = True
user_choice = ""

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(user_choice)
    if user_choice == "report":
        #print(resources)
        coffee_maker_module.report()
        coffee_maker_money_module.report()
    elif user_choice == "stop":
        break
    else:
        user_coffee_choice = coffee_menu.find_drink(user_choice)
        if coffee_maker_module.is_resource_sufficient(user_coffee_choice) and coffee_maker_money_module.make_payment(user_coffee_choice.cost):
            coffee_maker_module.make_coffee(user_coffee_choice)
