Slytherin =(0)
Hufflepuff =(0)
Ravenclaw =(0)
Gryffindor =(0)

print("1) Dawn")
print("2) Dusk")
Q1 = int(input('Q1) Do you like Dawn or Dusk? '))

print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
Q2 = int(input("Q2) When I'm dead, I want people to remember me as: "))

print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
Q3 = int(input("Q3) Which kind of instrument most pleases you ear? "))


if Q1 == 1:
  Gryffindor == +1 and Ravenclaw == +1


elif Q1 == 2:
  Hufflepuff = +1 and Slytherin == +1

else:
  print("Wrong input.")

if Q2 == 1:
  Hufflepuff == +2

elif Q2 == 2:
  Slytherin == +2

elif Q2 == 3:
  Ravenclaw == +2

elif Q2 == 4:
  Gryffindor == +2

else:
  print("Wrong input.")

if Q3 == 1:
  Slytherin == +4

elif Q3 == 2:
  Hufflepuff = +4

elif Q3 == 3:
  Ravenclaw = +4

elif Q3 == 4:
  Gryffindor = +4

else:
  print("Wrong input.")


if Slytherin >= 4:
  print("Slytherin")

elif Hufflepuff >= 4:
  print("Hufflepuff")

elif Ravenclaw >= 4:
  print("Ravenclaw")

else:
  print("Gryffindor")
