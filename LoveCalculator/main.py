print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

namesToGether = name1 + name2
namesTogether = namesTogether.lower()
##True
tCounter = 0
for letter in namesToGether:
  if('True'.find(letter) >= 1):
    tCounter += 1

##Love
lCounter = 0
for letter in namesToGether:
  if('Love'.find(letter) >= 1):
    lCounter += 1
totalCount = str(tCounter) + str(lCounter)

if(int(totalCount) < 10 or int(totalCount)> 90):
  print(f"Your score is {totalCount}, you got together like coke and mentos.")
elif(int(totalCount) >= 40 or int(totalCount)<= 50):
  print(f"Your score is {totalCount}, you are alright together.")
else:
  print(f"Your score is {totalCount}")
  
