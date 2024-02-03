user = input('Rock Paper or Scissors? ')

import random

num = random.randint(0, 2)

if num == 0:
    print("Rock")

elif num == 1:
    print("Paper")

else:
    print("Scissors")
