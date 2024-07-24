dog = ["Roger", "Syd", "Beau"]
print(dog)
player_dog = input("Which dog do you want? ")

if player_dog == "Roger":
  print("Congrats Roger is now yours")
elif player_dog == "Syd":
  print("Congrats Syd is now yours")
elif player_dog == "Beau":
  print("Congrats Beau is now yours")
else:
  print("Invalid Input")
  quit()

yes_or_no_change = input("Do you want to change your dog's name? (Y/N) ")


if yes_or_no_change == "Y":
  dog_name = input("What would you want your dog's name to be? ")
else:
  print("Ok, thanks for playing!")

if player_dog == "Roger":
  dog[0] = dog_name
  print("Congrats " + dog_name + "is now yours")
elif player_dog == "Syd":
  dog[1] = dog_name
  print("Congrats " + dog_name + "is now yours")
elif player_dog == "Beau":
  dog[2] = dog_name
  print("Congrats " + dog_name + "is now yours")
else:
  print("Invalid Input")
  quit()

print(dog)

dogies = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
print(dogies)