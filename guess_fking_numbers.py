import random

def start_game():
  print("Random number has been fucking picked!")
  return(random.randint(1,10))

def guess():
  print("What's your fucking guess between 1 and 10?")
  return(int(input('> ')))
  
def check(x,y):
  if y == x:
    print("You got it right, dumbass!")
    return(1)
  elif y < x:
    print("Too low, you dipshit!")
    return(0)
  elif y > x:
    print("Too high, you pothead!")
    return(2)
  
def play_again():
  playy = input("> ")
  if playy == 'Yes':
    return(1)
  elif playy == 'No':
    return(0)

while True:
  start = start_game()
  count = 5
  while count > 0:
    user_guess = guess()
    count = count - 1
    if check(start,user_guess) == 1:
      break
    print("You've got {} more guesses, you pig.".format(str(count)))
      
  print("Game over, LOSER! Play again, LOSER? Yes or No?")
  
  if play_again() == 0:
    break