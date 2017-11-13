import unittest
import polynanna
import data
from run_drawing import *
from pony.orm import *



class TestPolynanna(unittest.TestCase):


    def setUp(self):
        self.polyanna = polynanna.main()
        print('Failcount: ', self.polyanna.failcount)


    def tearDown(self):
        del self.polyanna


    def test_drawing_validity(self):
        for p in self.polyanna.participants:
            with self.subTest(p=p):
                self.assertIsNotNone(p.giving_to,
                             msg='giving_to not assigned for {}'.format(p.name))
                self.assertNotIn(p.giving_to, p.restricted_set,
                                 msg='Invalid {} giving_to'.format(p.name))


    def test_restricted_sets(self):
        for p in self.polyanna.participants:
            r_set = set(data.data.get(p.name))|set([y[1] for y in data.history.get(p.name)])
            with self.subTest(p=p):
                self.assertEqual(p.restricted_set, r_set)


    def test_participant_length(self):
        self.assertEqual(len(self.polyanna.participants), len(data.data.keys()))

    @unittest.skip('Skip Restricted Set Printing')
    def test_print_all_restricted_set(self):
        for p in self.polyanna.participants:
            print(p.name, 'restricted_set:', p.restricted_set)

    @unittest.skip('Skip Results Printing')
    def test_print_results(self):
        """Print results to the console."""
        for participant in self.polyanna.participants:
            print('{:<9} -->  {}'.format(participant.name, participant.giving_to))


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.polyanna = polynanna.main()
        db = Database()
        db.bind(provider='sqlite', filename='participants.db')
        db.generate_mapping(create_tables=True)


    def tearDown(self):
        del self.polyanna

    @db_session
    def test_print_database(self):
        self.assertEqual(len(self.polyanna.participants), len(Person.select()))
        print('participants.db Results')
        print('{:<9} |||  {} \n'.format('Name', 'Giving To'))
        for p in Person.select():
            print('{:<9} -->  {} \n'.format(p.name, p.giving_to), end='')
        

if __name__ == '__main__':
    unittest.main()
