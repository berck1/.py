import random

def get_choices():
  player_choice = input("Enter a choice rock, paper, scissors: ")
  player_choice = str(player_choice.lower())
  computer_options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(computer_options)
  choices = {"Player": player_choice, "Computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return print("It's a tie!")
  elif player == "rock":
    if computer == "scissors":
      return print("Rock smashes scissors! You win!")
    else:
      return print("Paper covers rock! You lose.")
  elif player == "paper":
    if computer == "rock":
      return print("Paper covers rock! You win!")
    else:
      return print("Scissors cuts paper! You lose.")
  elif player == "scissors":
    if computer == "paper":
      return print("Scissors cuts paper! You win!")
    else:
      return print("Rock smashes scissors! You lose.")
  else:
    return print("Invalid input. Please try again.")

choices = get_choices()
results = check_win(choices["Player"], choices["Computer"])