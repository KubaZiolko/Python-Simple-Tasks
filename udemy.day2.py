# def opcja1(1):
#     return "wybrano opcje 1"


# def opcja2(2):
#     return "wybrano opcje 1"

tip = 0
print("Welcome to the tip calculator !")
bill = float(input("How much was the total bill?$ "))
wybor = int(input("Would you like to give a tip? 1: yes , 0: No \n"))

match wybor : 
    case 1:
        tip = float(input("How much tip would you like to give? 10,12, or 15?"))
    case 0:
        print("You chose no tip.")
        tip = 0  # Domyślnie brak napiwku
    case _:
        print("Invalid choice.")
        exit()  # Jeśli użytkownik wpisze coś innego, kończymy program

people = int(input("How many people to split the bill? "))

total_pay = (bill + (bill*tip / 100)) / people
print(f"Each person should pay:{total_pay:.2f}$")
