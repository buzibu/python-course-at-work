import random

max_tries = 5

while True:
    machine_num = random.randint(1, 10)
    print('machine number: {}'.format(machine_num))
    tries = 0
    while tries < max_tries:
        user_number = int(input("Guess the number between 1 and 10 > "))
        if user_number < machine_num:
            print("your number is less than mine")
        elif user_number > machine_num:
            print("your number is more than mine")
        else:
            print("Congratulations!")
            break
        tries += 1
    if tries == max_tries:
        print('You loose! My number was {}'.format(machine_num))
    if str(input("Play once again? Y/N > ")).upper() == 'N':
        break
print("Good bye")


