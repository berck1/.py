import time
import random
generator0 = None
generator1 = None
generator2 = None
generator3 = None
confirm = None
credit_number0 = input("The 1st sequence of your credit card number: ")
credit_number1 = input("The 2nd: ") 
credit_number2 = input("The 3rd: ")
credit_number3 = input("The 4th: ")


print("Please Confirm your credit card number:")
credit_number = [f"{credit_number0}-{credit_number1}-{credit_number2}-{credit_number3}"]
for x in credit_number:
        print(x)
print()
credit_number = (f"{credit_number0}-{credit_number1}-{credit_number2}-{credit_number3}")
while not confirm == "Y" or "N":
        confirm = input("Confirm? [Y or N]: ")
        if confirm == "Y":
            time.sleep(2)
            print("Processing...")
            time.sleep(5)
            generator0 = random.randint(0, 3)
            generator1 = random.randint(0, 3)
            generator2 = random.randint(0, 3)
            generator3 = random.randint(0, 3)
            print(f"Your credit card number has been confirmed.")
            security0 = int(credit_number0[generator0])
            security1 = int(credit_number1[generator1])
            security2 = int(credit_number2[generator2])
            security3 = int(credit_number3[generator3])
            generator0 = generator0 + 1
            generator1 = generator1 + 1
            generator2 = generator2 + 1
            generator3 = generator3 + 1
            if generator0 == 1:
                generator0 = "1st"
            elif generator0 == 2:
                  generator0 = "2nd"
            elif generator0 == 3:
                  generator0 = "3rd"
            elif generator0 == 4:
                  generator0 = "4th"
            if generator1 == 1:
                generator1 = "1st"
            elif generator1 == 2:
                  generator1 = "2nd"
            elif generator1 == 3:
                  generator1 = "3rd"
            elif generator1 == 4:
                  generator1 = "4th"
            if generator2 == 1:
                generator2 = "1st"
            elif generator2 == 2:
                  generator2 = "2nd"
            elif generator2 == 3:
                  generator2 = "3rd"
            elif generator2 == 4:
                  generator2 = "4th"
            if generator3 == 1:
                generator3 = "1st"
            elif generator3 == 2:
                  generator3 = "2nd"
            elif generator3 == 3:
                  generator3 = "3rd"
            elif generator3 == 4:
                  generator3 = "4th"
            check0 = int(input(f"Enter the {generator0} digit of your credit card number in the {credit_number0} sequence: "))
            check1 = int(input(f"Enter the {generator1} digit of your credit card number in the {credit_number1} sequence: "))
            check2 = int(input(f"Enter the {generator2} digit of your credit card number in the {credit_number2} sequence: "))
            check3 = int(input(f"Enter the {generator3} digit of your credit card number in the {credit_number3} sequence: "))
            check0 = int(check0)
            check1 = int(check1)
            check2 = int(check2)
            check3 = int(check3)
            if check0 == security0 and check1 == security1 and check2 == security2 and check3 == security3:
                print("Your credit card number has been confirmed.")
                print("Thank you for confirming your credit card number.")
                exit()
            else:
                print("Credit Card Number Denied! Exiting...")
                exit()
        print("Your credit card number has been confirmed.")
        exit()
else:
        print("Credit Card Number Denied! Exiting...")
        exit()
