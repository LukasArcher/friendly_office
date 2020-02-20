from Office_2_with_tests.friendly_office import Office


class TurnOnTheBot:
    def __init__(self, bot, *numbers, **queues):
        self.my_office = Office(bot, *numbers, **queues)
        self.secret_password = "i hate this office"

    def turn_on_the_bot(self, secret):
        if self.my_office.bot == 'a':
            if self.my_office.number_a > 999:
                self.my_office.number_a = 0
            return self.my_office.add_applicant()

        elif self.my_office.bot == 'b':
            if self.my_office.number_b > 999:
                self.my_office.number_b = 0
            return self.my_office.add_applicant()

        elif self.my_office.bot == 'c':
            if self.my_office.number_c > 999:
                self.my_office.number_c = 0
            return self.my_office.add_applicant()

        elif self.my_office.bot == self.secret_password:
            return TurnOnTheBot.secret_mode(self, secret)

        elif self.my_office.bot == 'exit':
            q_a, q_b, q_c = [self.my_office.queue_a, self.my_office.queue_b, self.my_office.queue_c]
            empty = ''
            dot = '.'
            nobody_left = '\nHurray! We have served all our applicants today!!!'
            somebody_left = "\nSorry, we are closing...was nice to have you here!\n" \
                            "You can come to us tomorrow from 9 a.m. again. All the best!"
            return ("\n\n\n\n"
                    f"In the queue A left {len(q_a)} applicants"
                    f"{empty if len(q_a) > 0 else dot} {q_a if len(q_a) > 0 else empty}\n"
                    f"In the queue B left {len(q_b)} applicants"
                    f"{empty if len(q_b) > 0 else dot} {q_b if len(q_b) > 0 else empty}\n"
                    f"In the queue C left {len(q_c)} applicants"
                    f"{empty if len(q_c) > 0 else dot} {q_c if len(q_c) > 0 else empty}\n"
                    f"{nobody_left if q_a == [] and q_b == [] and q_c == [] else somebody_left}")

        else:
            return ("\n\n\n\nWTF are you doing dude!? Are you fucking illiterate or what?!"
                    "\n              READ CAREFULLY AND TRY AGAIN!\n\n\n\n")

    def secret_mode(self, secret):
        if secret == 'a':
            return self.my_office.remove_applicant_a()

        elif secret == 'b':
            return self.my_office.remove_applicant_b()

        elif secret == 'c':
            return self.my_office.remove_applicant_c()

        elif secret == 'exit':
            return "\n\n\n\nPfff, whatever...closing secret mode.\n\n\n\n"

        else:
            return "\n\n\n\nYou fucked it up...FFS, don't mess up with me!\n\n\n\n"
