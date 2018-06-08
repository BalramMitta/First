l=0
h=100
m=0
g='l'
print("Please think of a number between 0 and 100!")
while g != 'c' :
  if g == 'l':
    l=m
  elif g == 'h':
    h=m
  else:
    print "Choose the correct input\n"
  m=(l+h)/2  
  print "Is your secret number ",m ,"?\n"
  g=raw_input("Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.:")
else:
  print "Game over. Your secret number was: ",m
