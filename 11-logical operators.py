temp = int(input("How warm is outside? (C°): "))
validation = ("true", "false")
is_raining = None
while is_raining not in validation:
    is_raining = input("Is it raining outside? (true or false): ")
if is_raining == "true":
    is_raining = True
else:
    is_raining == False


if temp > 30 or is_raining == True:
    print("Dont go outside.")
else:
    print("You can go outside.")

