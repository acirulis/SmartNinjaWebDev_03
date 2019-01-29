from random import randint

secret_number = randint(1,100)

is_correct = False

while not is_correct:
    user_guess = int(input("Please make your guess between 1 and 100: "))

    if user_guess > secret_number:
        print('Real number is smaller.')
    elif user_guess < secret_number:
        print('Real number is larger.')
    else:
        print('You are correct!')
        is_correct = True



