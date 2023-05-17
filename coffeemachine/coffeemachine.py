def make_espresso():
    print("starting to make espresso")
    print("grinding coffee beans")
    print("boiling water")
    print("mixing boiled water with crushed coffee beans")
    print("pouring coffee into the cup")
    print("Expresso is ready!")
def make_cappuccino():
    print("starting to make cappuccino")
    print("grinding coffee beans")
    print("boiling water")
    print("mixing boiled water with crushed coffee beans")
    print("pouring coffee into the cup")
    print("frothing milk")
    print("Pouring frothed milk into the cup")
    print("Cappuccino is ready!")
def make_late():
    print("Starting to make a latte")
    print("Grinding coffee beans")
    print("Boiling water")
    print("Mixing boiled water with crushed coffee beans")
    print("Pouring coffee into the cup")
    print("Frothing milk")
    print("Pouring frothed milk into the cup")
    print("Latte is ready!")
def calculate_ingridients(num_cups):
    water=num_cups*200
    milk=num_cups*50
    coffee_beans=num_cups*15
    print(f"For {num_cups} cups of coffee U will need:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{coffee_beans} g of coffee beans")
num_of_cups=int(input("how many cups of coffee U will need?:"))
calculate_ingridients(num_of_cups)