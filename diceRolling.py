from random import randint

def rolling():
  while True:
      user_input = input('Do you want to roll? Y/N ')

      if user_input.lower() == 'n':
          print('No more rolling')
          break
      elif user_input.lower() == 'y':
          print(randint(1,6))
      # User enters anything other than y or n
      else:
          print('Please enter in a Y or N')

rolling()
