import random

def computer_choice():
    if computer == rock:
        computer_choice = 'rock'.capitalize()
    elif computer == paper:
        computer_choice = 'paper'.capitalize()
    else:
        computer_choice = 'scissors'.capitalize()
    print(f"Computer choice: {computer_choice}")

def player_choice():
    if player == 'rock':
        print(rock)
    elif player == 'paper':
        print(paper)
    else:
        print(scissors)

rock = ['rock','''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''']

paper = ['paper',''''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''']

scissors = ['scissors', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

while True:
    # Player choose
    player = input("Enter a choice (Rock, Paper, Scissors): ").lower()
    print(f"Player choose: {player.capitalize()}")
    player_choice()

    # Computer choose
    computer = random.choice([rock, paper, scissors])
    computer_choice()
    print(computer)

    # Logic handling
    if player == computer:
        print("It's Draw")


