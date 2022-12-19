bot_name = "DICKTBOT"
birth_year = "8.10.2022"


print("Hello! My name is,", bot_name,)
print("I was created in ", birth_year,)
print("Please remind me your name: ")
user_name = input()

print("What a great name u have", user_name, "!")
print("Let me guess your age")
print("Enter you age +1 year +2 n +3")

user_age1 = int(input("Age +1: "))
user_age2 = int(input("Age +2: "))
user_age3 = int(input("Age +3: "))
user_age = int((user_age1 * 15 + user_age2 * 21 + user_age3 * 70) % 105)
print("You age is", user_age)
user_number = int(input("Now i will prove to u that I can count to any number you want :"))
number = 1
while number <= user_number:
    print(number)
    number += 1
else:
    print("Complete")
test = int(input("Let's do a test" "\nWhat is int?" "\n1. Integer" "\n2. String" "\n3. Nothing" "\n4. Nothing 2.0" "\n"))
while test != 1:
    test = int(input("Wrong answer, repeat" "\n"))
else:
    test = 1
    print("Congratulations, have a nice day!")
