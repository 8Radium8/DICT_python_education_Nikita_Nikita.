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
class CoffeeMachine:
    def __init__(self):
        self.water=400
        self.milk=540
        self.coffee_beans=120
        self.disposable_cups=9
        self.money=550
    def print_state(self):
        print("Coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} g of coffee beans")
        print(f"{self.disposable_cups} of cups")
        print(f"{self.money} of money")
    def can_make_coffee(self, water_needed, milk_needed, coffee_beans_needed, cost):
        if self.water < water_needed:
            return "water"
        if self.milk < milk_needed:
            return "milk"
        if self.coffee_beans < coffee_beans_needed:
            return "coffe beans"
        if self.disposable_cups < 1:
            return "disposable cups"
        return "yes"
    def make_coffee(self,water_needed, milk_needed, coffee_beans_needed, cost):
        if self.can_make_coffee(water_needed, milk_needed, coffee_beans_needed)=="yes":
            print("I have enough resources to make coffee...")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= coffee_beans_needed
            self.disposable_cups -= 1
            print("Coffee is ready!\n")
    def buy_coffee(self):
        print("What do u prefer? 1 - espresso \n2 - capuccino \n3 - late")
        choice = input()
        if choice == "1":
            self.make_coffee(250, 0, 16, 4)
        elif choice == "2":
            self.make_coffee(200, 100, 12, 6)
        elif choice =="3":
            self.make_coffee(350, 75, 20, 7)
        else:
            print("invalid choice \n")
    def fill_machine(self):
        print("how many ml of water u want to add?:")
        water_added = int(input())
        print("how many ml milk u want to add?:")
        milk_added = int(input())
        print("how many grams of coffee beans u want to add?:")
        coffee_beans_added = int(input())
        print("how many cups u want to add?:")
        cups_added = int(input())

        self.water += water_added
        self.milk += milk_added
        self.coffee_beans += coffee_beans_added
        self.disposable_cups += cups_added
    def take_money(self):
        print(f"I gave u ${self.money}")
        self.money = 0

coffee_machine = CoffeeMachine()

while True:
    coffee_machine.print_state()
    print("print action(buy, fill, take):")
    action=input()
    if action == "buy":
        coffee_machine.buy_coffee()
    elif action=="fill":
        coffee_machine.fill_machine()
    elif action=="take":
        coffee_machine.take_money()
    else:
        print("Invalid action!\n")