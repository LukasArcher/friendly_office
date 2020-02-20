from Office_2_with_tests.turn_on_the_bot import TurnOnTheBot as MyOffice
from time import sleep


if __name__ == '__main__':
    numbers = [0, 0, 0]
    queues = {'queue_a': [], 'queue_b': [], 'queue_c': []}
    bot = ''
    secret = ''
    time = 2

    while bot != 'exit':
        bot = input("""Hi man, what's up?
I wish you a great time in our the most friendly office!
(pssst, the secret password is - 'I hate this office')

Look, here we have 3 queues, to choose one of them type:
'A' - for vehicle registration
'B' - for driving license
'C' - for ID card
and then you gonna get your ticket: """).lower()

        if bot == 'a':
            numbers[0] += 1
        elif bot == 'b':
            numbers[1] += 1
        elif bot == 'c':
            numbers[2] += 1

        my_office = MyOffice(bot, *numbers, **queues)

        if bot == my_office.secret_password:
            secret = input("""\n\n\n\nDude! You're in the secret mode now! Awesome!
                Type A, B or C according on which applicant you want to call out
                or type "exit" if you want to close the secret mode: """).lower()

        print(my_office.turn_on_the_bot(secret))
        sleep(time)

        if bot == my_office.secret_password:
            while secret not in ['a', 'b', 'c', 'exit']:
                secret = input("""\n\n\n\nDude! You're in the secret mode now! Awesome!
                                Type A, B or C according on which applicant you want to call out
                                or type "exit" if you want to close the secret mode: """).lower()
                print(my_office.secret_mode(secret))
                sleep(time)
