loop = True
num3 = False
while loop == True:
    continue_ = input("Would you like to continue this program? (Y or N): ")
    if continue_ == "Y":
        if num3 == True:
            print(num3)
            operator = input("Enter your operator (+ - / *) ")
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
            if operator == "+":
                num3 = num2 + num1
                print(num3 + num1 + num2)
            elif operator == "-":
                num3 = num2 - num1
                print(num3 + num1 - num2)
            elif operator == "/":
                num3 = num2 / num1
                print(num3 + num1 / num2)
            elif operator == "*":
                num3 = num2 * num1
                print(num3 + num1 * num2)
            else:
                print("Wrong input! Try again.")
                exit()
        else:
            operator = input("Enter your operator (+ - / *) ")
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
            if operator == "+":
                num3 = num2 + num1
                print(num1 + num2)
            elif operator == "-":
                num3 = num2 - num1
                print(num1 - num2)
            elif operator == "/":
                num3 = num2 / num1
                print(num1 / num2)
            elif operator == "*":
                num3 = num2 * num1
                print(num1 * num2)
            else:
                print("Wrong input! Try again.")
                exit()
    elif continue_ == "N":
            print("Exiting...")
            exit()
    else:
            print("Wrong input. Exiting...")
            exit()