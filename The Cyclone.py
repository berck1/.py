height = int(input('How tall are you (cm)? '))
credits = int(input('How much credits do you have? '))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")

elif credits >= 10 and height < 137:
  print("You are not tall enough to ride.")

elif height >= 137 and credits < 10:
  print("You don't have enough credits.")

else:
  print("You haven't got any of these requirements.")