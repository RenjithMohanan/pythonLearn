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

choice = input('Rock Paper Scissors ... ')
game =[rock,paper,scissors]
if(choice == '0' or choice == '1' or choice == '2'):
  print(game[int(choice)])
  import random
  randomPlay = random.randint(0,2)
  print(randomPlay)

  print(game[randomPlay])
  if(int(choice) == 0 and randomPlay == 1):
    print("You lose!")
  elif(int(choice) == 0 and randomPlay == 2):
    print("You WIN!!!!")
  elif(int(choice) == 1 and randomPlay == 0):
    print("You WIN!!!!")
  elif(int(choice) == 1 and randomPlay == 2):
    print("You lose!")
  elif(int(choice) == 2 and randomPlay == 0):
    print("You lose!")
  elif(int(choice) == 2 and randomPlay == 1):
    print("You WIN!!!!")
else:
  print('Wrong play! Try again...')
