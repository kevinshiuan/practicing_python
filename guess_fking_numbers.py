import random

def start_game(z):
  print("Random number has been fucking picked! You have 5 stupid guesses...")
  return(random.randint(1,z))

def guess():
  while True:
  	try:
  		y = int(input("What's your fucking guess between 1 and 10?: "))
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

high_num = 10
count = 5

while True:
  start = start_game(high_num)
  guesses = []
  while count - len(guesses) > 0:
    user_guess = guess()
    if check(start,user_guess) == 1:
      break
    guesses.append(user_guess)
    print("You've got {} more guesses, you pig. You previously fucking guessed {}".
    	format(str(count - len(guesses)),str(', '.join(str(e) for e in guesses))))

  y = input("Game over, LOSER! Play again, LOSER? 1 for yes, 0 for no -_-: ")
  
  if y == 0:
    break