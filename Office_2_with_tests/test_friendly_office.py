import unittest
from Office_2_with_tests.friendly_office import Office
from random import randrange
# from turn_on_the_bot import TurnOnTheBot
# from unittest.mock import Mock, MagicMock, patch


class TestFriendlyOffice(unittest.TestCase):
    def setUp(self) -> None:
        self.numbers = [randrange(0, 1000), randrange(0, 1000), randrange(0, 1000)]
        self.queues = {'queue_a': [], 'queue_b': [], 'queue_c': []}
        self.letters = ['a', 'b', 'c']
        self.random_l = randrange(0, 2)
        self.office = Office(self.letters[self.random_l], *self.numbers, **self.queues)

    def test_add_applicant(self):
        self.office = Office('a', *self.numbers, **self.queues)
        self.add_applicant = self.office.add_applicant()
        if self.office.bot == 'a':
            self.office = Office('a', *self.numbers, **self.queues)
            if self.numbers[0] < 10:
                self.queues['queue_a'].append(f"A00{self.numbers[0]}")
                result = f"\n\n\n\n      {self.queues['queue_a'][-1]}\n\n\n\n"
            elif 100 > self.numbers[0] >= 10:
                self.queues['queue_a'].append(f"A0{self.numbers[0]}")
                result = f"\n\n\n\n      {self.queues['queue_a'][-1]}\n\n\n\n"
            else:
                self.queues['queue_a'].append(f"A{self.numbers[0]}")
                result = f"\n\n\n\n      {self.queues['queue_a'][-1]}\n\n\n\n"
            self.assertEqual(result, self.add_applicant)

        self.office = Office('b', *self.numbers, **self.queues)
        self.add_applicant = self.office.add_applicant()
        if self.office.bot == 'b':
            self.office = Office('b', *self.numbers, **self.queues)
            if self.numbers[1] < 10:
                self.queues['queue_b'].append(f"B00{self.numbers[1]}")
                result = f"\n\n\n\n      {self.queues['queue_b'][-1]}\n\n\n\n"
            elif 100 > self.numbers[1] >= 10:
                self.queues['queue_b'].append(f"B0{self.numbers[1]}")
                result = f"\n\n\n\n      {self.queues['queue_b'][-1]}\n\n\n\n"
            else:
                self.queues['queue_b'].append(f"B{self.numbers[1]}")
                result = f"\n\n\n\n      {self.queues['queue_b'][-1]}\n\n\n\n"
            self.assertEqual(result, self.add_applicant)

        self.office = Office('c', *self.numbers, **self.queues)
        self.add_applicant = self.office.add_applicant()
        if self.office.bot == 'c':
            self.office = Office('c', *self.numbers, **self.queues)
            if self.numbers[2] < 10:
                self.queues['queue_c'].append(f"C00{self.numbers[2]}")
                result = f"\n\n\n\n      {self.queues['queue_c'][-1]}\n\n\n\n"
            elif 100 > self.numbers[2] >= 10:
                self.queues['queue_c'].append(f"C0{self.numbers[2]}")
                result = f"\n\n\n\n      {self.queues['queue_c'][-1]}\n\n\n\n"
            else:
                self.queues['queue_c'].append(f"C{self.numbers[2]}")
                result = f"\n\n\n\n      {self.queues['queue_c'][-1]}\n\n\n\n"
            self.assertEqual(result, self.add_applicant)

    def test_remove_applicant_a(self):
        if self.office.bot == 'a':
            self.office.add_applicant()
            if self.numbers[0] < 10:
                self.queues['queue_a'].append(f"A00{self.numbers[0]}")
            elif 100 > self.numbers[0] >= 10:
                self.queues['queue_a'].append(f"A0{self.numbers[0]}")
            else:
                self.queues['queue_a'].append(f"A{self.numbers[0]}")
        if not self.queues['queue_a'] == []:
            removed_applicant = self.queues['queue_a'].pop(0)
            result = f"\n\n\n\nNext applicant: {removed_applicant}\n\n\n\n"
            self.assertEqual(result, self.office.remove_applicant_a())
        else:
            result = "\n\n\n\nMan, nobody left in this queue...\n\n\n\n"
            self.assertEqual(result, self.office.remove_applicant_a())

    def test_remove_applicant_b(self):
        if self.office.bot == 'b':
            self.office.add_applicant()
            if self.numbers[1] < 10:
                self.queues['queue_b'].append(f"B00{self.numbers[1]}")
            elif 100 > self.numbers[1] >= 10:
                self.queues['queue_b'].append(f"B0{self.numbers[1]}")
            else:
                self.queues['queue_b'].append(f"B{self.numbers[1]}")
        if not self.queues['queue_b'] == []:
            removed_applicant = self.queues['queue_b'].pop(0)
            result = f"\n\n\n\nNext applicant: {removed_applicant}\n\n\n\n"
            self.assertEqual(result, self.office.remove_applicant_b())
        else:
            result = "\n\n\n\nMan, nobody left in this queue...\n\n\n\n"
            self.assertEqual(result, self.office.remove_applicant_b())

    def test_remove_applicant_c(self):
        if self.office.bot == 'c':
            self.office.add_applicant()
            if self.numbers[2] < 10:
                self.queues['queue_c'].append(f"C00{self.numbers[1]}")
            elif 100 > self.numbers[2] >= 10:
                self.queues['queue_c'].append(f"C0{self.numbers[1]}")
            else:
                self.queues['queue_c'].append(f"C{self.numbers[1]}")
        if not self.queues['queue_c'] == []:
            removed_applicant = self.queues['queue_c'].pop(0)
            result = f"\n\n\n\nNext applicant: {removed_applicant}\n\n\n\n"
            self.assertEqual(result, self.office.remove_applicant_c())
        else:
            result = "\n\n\n\nMan, nobody left in this queue...\n\n\n\n"
            self.assertEqual(result, self.office.remove_applicant_c())


# class TestTurnOnTheBot(unittest.TestCase):
#    def test_turn_on_the_bot(self):
#        self.mock_office = Mock()
#        self.mock_office.add_applicant = MagicMock(return_value='a')
#        with patch.object(TurnOnTheBot, "turn_on_the_bot", return_value='test') as new_mock:
#            self.bot_1 = TurnOnTheBot('test')
#            self.assertEqual(self.bot_1.turn_on_the_bot('secret'), 'a')
