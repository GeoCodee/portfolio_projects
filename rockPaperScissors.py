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
---'   ____)____
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

#Write your code below this line 👇
moves =[rock,paper,scissors]
computer_choice = random.randint(0,2)
computer_move = moves[computer_choice]

win ="You Win."
lose ="You Lose."
draw ="It's a draw."


choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, or '2' for Scissors: "))
print(moves[choice])

print(f"The Computer Selected: \n {moves[computer_choice]}")

if choice == 0:
  if(computer_choice == 0):
    print(draw)
  elif(computer_choice == 1):
    print(lose)
  else:
    print(win)
elif choice == 1:
  if(computer_choice == 0):
    print(win)
  elif(computer_choice == 1):
    print(draw)
  else:
    print(lose)
elif choice == 2:
  if(computer_choice == 0):
    print(lose)
  elif(computer_choice == 1):
    print(win)
  else:
    print(draw)
else:
  print("Your input doesn't select rock, paper, or scissors. Please try again")