from replit import db
import datetime, time, os

def menu():
  print()
  ask = input('Enter:\n1. Add Tweet\n2. View Tweet\n>> ')
  return ask

def add():
  tweet = input("\033[0mEnter your tweet here🐥 > ")
  a = datetime.datetime.now()
  key = f"mes{a}"
  db[key] = tweet
  time.sleep(1)
  print()
  print('\033[32mTweet Added Succesfully😎\033[0m')
  time.sleep(1)
  os.system("clear")

def view():
  global f
  matches = db.prefix("mes")
  matches = matches[::-1]
  y= 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(3)
    y +=1
    if y % 10 == 0:
      ask = input("Do you want to view another 10 tweets? y/n ")
      if ask.lower() != "y" :
        break
  time.sleep(1)
  os.system("clear")


while True:
  print("\033[4mWELCOME TO MY TWEETER\033[0m")
  c = menu()
  if c == "1":
    add()
  elif c == '2':
    view()
  else:
    print()
    print('\033[31mInvalid Selection!')
    time.sleep(1)
    continue