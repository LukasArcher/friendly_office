class Office:

    def __init__(self):
        self.bot = input("""Hi man, what's up?
I wish you a great time in our the most friendly office!
(pssst, the secret password is - 'I hate this office')

Look, here we have 3 queues, to choose one of them type:
'A' - for vehicle registration
'B' - for driving license
'C' - for ID card
and then you gonna get your ticket: """).lower()

        self.number_a = 8
        self.number_b = 98
        self.number_c = 998
        self.queue_a = []
        self.queue_b = []
        self.queue_c = []

    def add_applicant(self):
        if self.bot == 'a':
            if self.number_a < 10:
                self.queue_a.append(f"A00{self.number_a}")
                print(f"\n\n\n\n      {self.queue_a[-1]}\n\n\n\n")
            elif 100 > self.number_a >= 10:
                self.queue_a.append(f"A0{self.number_a}")
                print(f"\n\n\n\n      {self.queue_a[-1]}\n\n\n\n")
            else:
                self.queue_a.append(f"A{self.number_a}")
                print(f"\n\n\n\n      {self.queue_a[-1]}\n\n\n\n")

        if self.bot == 'b':
            if self.number_b < 10:
                self.queue_b.append(f"B00{self.number_b}")
                print(f"\n\n\n\n      {self.queue_b[-1]}\n\n\n\n")
            elif 100 > self.number_b >= 10:
                self.queue_b.append(f"B0{self.number_b}")
                print(f"\n\n\n\n      {self.queue_b[-1]}\n\n\n\n")
            else:
                self.queue_b.append(f"B{self.number_b}")
                print(f"\n\n\n\n      {self.queue_b[-1]}\n\n\n\n")

        if self.bot == 'c':
            if self.number_c < 10:
                self.queue_c.append(f"C00{self.number_c}")
                print(f"\n\n\n\n      {self.queue_c[-1]}\n\n\n\n")
            elif 100 > self.number_c >= 10:
                self.queue_c.append(f"C0{self.number_c}")
                print(f"\n\n\n\n      {self.queue_c[-1]}\n\n\n\n")
            else:
                self.queue_c.append(f"C{self.number_c}")
                print(f"\n\n\n\n      {self.queue_c[-1]}\n\n\n\n")

    def remove_applicant_a(self):
        if not self.queue_a == []:
            removed_applicant = self.queue_a.pop(0)
            print(f"\n\n\n\nNext applicant: {removed_applicant}\n\n\n\n")
        else:
            print("\n\n\n\nMan, nobody left in this queue...\n\n\n\n")

    def remove_applicant_b(self):
        if not self.queue_b == []:
            removed_applicant = self.queue_b.pop(0)
            print(f"\n\n\n\nNext applicant: {removed_applicant}\n\n\n\n")
        else:
            print("\n\n\n\nMan, nobody left in this queue...\n\n\n\n")

    def remove_applicant_c(self):
        if not self.queue_b == []:
            removed_applicant = self.queue_b.pop(0)
            print(f"\n\n\n\nNext applicant: {removed_applicant}\n\n\n\n")
        else:
            print("\n\n\n\nMan, nobody left in this queue...\n\n\n\n")

