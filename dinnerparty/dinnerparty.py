import random
much_person = []

def count():
    print("How much friends will be on party?")
    number_person = int(input(":>"))
    if number_person <= 1:
        print("Do You have no friends?" "\nI don't think so!")
        return
    print("Type names of your friends which will be on your party")
    for i in range(number_person):
        input_person = input(":>")
        much_person.append(input_person)
    input_amount =int(input("How much you paid for meal?" "\n:>"))
    lucky_one = input("Do you want to spin the wheel of fortune and choose the lucky one?" "\nType Yes or No" "\n:>")
    choice_lucky = random.choice(much_person)
    if lucky_one == "Yes":
        number_person -= 1
        print(f"{choice_lucky} Here is our lucky guy")
    else:
        print("Are you such a greedy friend that you don't want to give your friends a chanse?" "\n")
    amount_person = round((input_amount / number_person), 2)
    print(amount_person)
count()