# Write your code here 👇
n=1
prinT = ''
for n in range (1 , 101, 1):
  prinT = ''
  if(n%3 == 0 ) :
    prinT ='Fizz'
  if(n%5 == 0) :
    prinT=prinT +'Buzz'
  if(n%5 != 0 and n%3 != 0):
    prinT = str(n)
  print(prinT)
