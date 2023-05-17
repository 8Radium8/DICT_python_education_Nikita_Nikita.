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
def check_resources(water, milk, coffee_beans, num_cups):
    cups_possible= min(water // 200, milk // 50, coffee_beans // 15)
    if cups_possible >= num_cups:
        if cups_possible == num_cups:
            print("Yes, I can make that amount of coffee")
        else:
            extra_cups = cups_possible-num_cups
            print(f"Yes, I can make that amount of coffee, and even {extra_cups} more than that")
    else:
        print(f"Sorryan, but i can make only {cups_possible} cups of coffee")
water_available = int(input("write how many ml of water machine has:"))
milk_available = int(input("write how many ml of milk machine has:"))
coffee_beans_available = int(input("write how many grams of coffee beans machine has:"))
num_of_cups=int(input("how many cups of coffee U will need?:"))
check_resources(water_available,milk_available,coffee_beans_available, num_of_cups)