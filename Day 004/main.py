import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print(map[human_choice])

computer_choice = random.randint(0, 2)

print("Computer chose: \n", map[computer_choice])

if human_choice == 0 and computer_choice == 1:
    print("You Lose!")
elif human_choice == 0 and computer_choice == 2:
    print("You Won!")
elif human_choice == 1 and computer_choice == 0:
    print("You Won!")
elif human_choice == 1 and computer_choice == 2:
    print("You Lose!")
elif human_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif human_choice == 2 and computer_choice == 1:
    print("You Won!")
else:
    print("Draw!")




