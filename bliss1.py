age = 0
name = ""
money = 0
bank = ""
select = ""
option = ""
option_money = 0
print("WELCOME TO:  B                V")
print("             L                I")
print("             I                B")
print("             S                E")
print("             S                S")


while name == "":
    name = input("Enter your name: ")
    if name == "":
        print("Please enter a valid input.")

while not age > 0:
    age = int(input("Enter your age: "))
    if not age >= 18:
        print("You must be atleast 18 years of age to attend BLISS VIBES!")
        exit()
    elif not age > 0:
        print("Age cannot be 0 or less.")
    
print("Here are the Tickets and their current prices:")
print("                    VIP                                         Semi-VIP                                       Normal                     ")
print("                    75$                                           50$                                           25$                       ")
while select == "":
    select = input("Select a ticket you would like to see: ")
    if select == "VIP":
        print("VIP has all the features available.")
        print("For more information, check out https://blissvibes.net")
        select1 = int(input("To see more features available from other tickets type 1, else type 2: "))
        if select1 == 1:
            print("Going back to 'feature' mode...")
            select = ""
        elif select1 == 2:
            print("Continuing process...")
            select = "VIP"
            break
        else:
            print("Invalid input, going to 'feature' mode...")
    elif select == "Semi-VIP":
        print("Semi-VIP has access to VIP features such as an exclusive site where you can stay and a customized Semi-VIP wristband.")
        print("For more information, check out https://blissvibes.net")
        select1 = int(input("To see more features available from other tickets type 1, else type 2: "))
        if select1 == 1:
            print("Going back to 'feature' mode...")
            select = ""
        elif select1 == 2:
            print("Continuing process...")
            select = "Semi-VIP"
            break
        else:
            print("Invalid input, going to 'feature' mode...")
    elif select == "Normal":
        print("Normal doesn't have any features rather than a normal wristband and the access to the site.")
        print("For more information, check out https://blissvibes.net")
        select1 = int(input("To see more features available from other tickets type 1, else type 2: "))
        if select1 == 1:
            print("Going back to 'feature' mode...")
            select = ""
        elif select1 == 2:
            print("Continuing process...")
            select = "Normal"
            break
        else:
            print("Invalid input, going to 'feature' mode...")
            select = ""
    elif not select == "VIP" or "Semi-VIP" or "Normal":
        select = ""


while option == "":
    option = input("Select your ticket: ")
    if option == "VIP":
        print("VIP ticket selected.")
    elif option == "Semi-VIP":
        print("Semi-VIP ticket selected.")
    elif option == "Normal":
        print("Normal ticket selected.")
    elif not option == "VIP" or "Semi-VIP" or "Normal":
        option = ""

print("Next up is your banking details.")

if option == "VIP":
    option_money = 75
elif option == "Semi-VIP":
    option_money = 50
else:
    option_money = 25


while bank == "":
    bank = input("Please select a payment processor (VISA, Mastercard): ")
    if bank == "VISA":
        print("VISA selected.")
        break
    elif bank == "Mastercard":
        print("Mastercard selected.")
        break
    elif not bank == "VISA" or "Mastercard":
        bank = ""

while not money > 0:
    money = int(input(f"Please enter how much money you have in your {bank} bank account: "))
    if money >= option_money:
        print(f"Transaction for {option} from payment processor {bank} of {option_money}$ has been successfully made.")
        money = money - option_money
        print(f"You now have {money}$ left.")
        print(f"Welcome to Bliss Vibes {name}!")
        break
    elif not money >= 0:
        print("Your ammount should not equal to less than 0$.")
        money = -1
    elif not money >= option_money:
        print("Not enough money to complete this transaction.")
        print("Exiting program...")
        exit()