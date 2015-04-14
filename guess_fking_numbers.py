import random

def start_game(z):
  print("Random number has been fucking picked!")
  return(random.randint(1,z))

def guess():
  while True:
  	x = input("What's your fucking guess between 1 and 10?: ")
  	
  	try:
  		y = int(x)
  		break
  	except:
  		print('That\'s not a fucking whole number! Try again...')
  		pass
  		
  return(y)
  
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

high_num = 10

while True:
  start = start_game(high_num)
  count = 5
  guesses = []
  while count - len(guesses) > 0:
    user_guess = guess()
    if check(start,user_guess) == 1:
      break
    print("You've got {} more guesses, you pig.".format(str(count)))
    user_guess.app(guesses)
      
  print("Game over, LOSER! Play again, LOSER? Yes or No?")
  
  if play_again() == 0:
    break