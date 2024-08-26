from getpass import getpass
pl = int(getpass("player 1: ")) 
while True:
  guess = int(input("guess the number: "))
  if guess == pl:
      print("you win")
  elif guess < pl:
      print("number is bigger")
  else:
      print("number is smaller")