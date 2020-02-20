from friendly_office import Office
from time import sleep


class TurnOnTheBot:
    def __init__(self):
        self.my_office = Office()
        self.sleep = 2
        self.secret_password = "i hate this office"

    def turn_on_the_bot(self):
        if self.my_office.bot == 'a':
            self.my_office.number_a += 1
            if self.my_office.number_a > 999:
                self.my_office.number_a = 0
            self.my_office.add_applicant()
            sleep(self.sleep)

        elif self.my_office.bot == 'b':
            self.my_office.number_b += 1
            if self.my_office.number_b > 999:
                self.my_office.number_b = 0
            self.my_office.add_applicant()
            sleep(self.sleep)

        elif self.my_office.bot == 'c':
            self.my_office.number_c += 1
            if self.my_office.number_c > 999:
                self.my_office.number_c = 0
            self.my_office.add_applicant()
            sleep(self.sleep)

        elif self.my_office.bot == self.secret_password:
            TurnOnTheBot.secret_mode(self)
        elif self.my_office.bot == 'exit':
            pass
        else:
            print("\n\n\n\nHey, What's wrong with you dude? Are you illiterate or what?\n\n\n\n")
            sleep(self.sleep)

        while self.my_office.bot != 'exit':
            self.my_office.bot = input("""Hi man, what's up?
I wish you a great time in our the most friendly office!

Look, here we have 3 queues, to choose one of them type:
'A' - for vehicle registration
'B' - for driving license
'C' - for ID card
and then you gonna get your ticket: """).lower()
            if self.my_office.bot == 'a':
                self.my_office.number_a += 1
                if self.my_office.number_a > 999:
                    self.my_office.number_a = 0
                self.my_office.add_applicant()
                sleep(self.sleep)

            elif self.my_office.bot == 'b':
                self.my_office.number_b += 1
                if self.my_office.number_b > 999:
                    self.my_office.number_b = 0
                self.my_office.add_applicant()
                sleep(self.sleep)

            elif self.my_office.bot == 'c':
                self.my_office.number_c += 1
                if self.my_office.number_c > 999:
                    self.my_office.number_c = 0
                self.my_office.add_applicant()
                sleep(self.sleep)

            elif self.my_office.bot == self.secret_password:
                TurnOnTheBot.secret_mode(self)
            elif self.my_office.bot == 'exit':
                pass
            else:
                print("\n\n\n\nWTF are you doing dude!? Are you fucking stupid?! READ CAREFULLY AND TRY AGAIN:\n\n\n\n")
                sleep(self.sleep)

        else:
            empty = ''
            dot = '.'
            print("\n\n\n\n")
            print(f"In the queue A left {len(self.my_office.queue_a)} applicants"
                  f"{empty if len(self.my_office.queue_a) > 0 else dot} "
                  f"{self.my_office.queue_a if len(self.my_office.queue_a) > 0 else empty}")
            print(f"In the queue B left {len(self.my_office.queue_b)} applicants"
                  f"{empty if len(self.my_office.queue_b) > 0 else dot} "
                  f"{self.my_office.queue_b if len(self.my_office.queue_b) > 0 else empty}")
            print(f"In the queue C left {len(self.my_office.queue_c)} applicants"
                  f"{empty if len(self.my_office.queue_c) > 0 else dot} "
                  f"{self.my_office.queue_c if len(self.my_office.queue_c) > 0 else empty}")

            print("\nSorry, we are closing...was nice to have you here!\n"
                  "You can come to us tomorrow from 9 a.m. again. All the best!")

    def secret_mode(self):
        while True:
            secret = input("""\n\n\n\nDude! You're in the secret mode now! Awesome!
Type A, B or C according on which applicant you want to call out
or type "exit" if you want to close the secret mode: """).lower()

            if secret == 'a':
                self.my_office.remove_applicant_a()
                sleep(self.sleep)
                break
            elif secret == 'b':
                self.my_office.remove_applicant_b()
                sleep(self.sleep)
                break
            elif secret == 'c':
                self.my_office.remove_applicant_c()
                sleep(self.sleep)
                break
            elif secret == 'exit':
                print("\n\n\n\nPfff, whatever...closing secret mode.\n\n\n\n")
                sleep(self.sleep)
                break
            else:
                print("\n\n\n\nYou fucked it up...FFS, don't mess up with me!\n\n\n\n")
                sleep(self.sleep)
