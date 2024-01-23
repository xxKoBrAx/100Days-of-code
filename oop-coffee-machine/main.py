from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

men = Menu()
c_maker = CoffeeMaker()
m_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? {men.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        f"{c_maker.report()}\n{m_machine.report()}"
    else:
        drink = men.find_drink(choice)
        if c_maker.is_resource_sufficient(drink):
            if m_machine.make_payment(drink.cost):
                c_maker.make_coffee(drink)
