from random import randint

while True:
    user_input = input('Do you want to roll? Y/N ')

    if user_input.lower() == 'n':
        print('No more rolling')
        break
    else:
        print(randint(1,6))
