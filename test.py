import unittest
import polynanna
import seed_db
from participants import participants, history
from pony.orm import *



class TestPolynanna(unittest.TestCase):

    def setUp(self):
        self.polyanna = polynanna.main()


    def tearDown(self):
        del self.polyanna


    def test_drawing_validity(self):
        for p in self.polyanna._participants:
            with self.subTest(p=p):
                self.assertIsNotNone(p.giving_to,
                             msg='giving_to not assigned for {}'.format(p.name))
                self.assertNotIn(p.giving_to, p.restricted_set,
                                 msg='Invalid {} giving_to'.format(p.name))


    def test_restricted_sets(self):
        """Test that restricted sets are equal to the intersections of restricted_set and history sets."""
        for p in self.polyanna._participants:
            r_set = set(participants.get(p.name))|set([y[1] for y in history.get(p.name)])
            with self.subTest(p=p):
                self.assertEqual(p.restricted_set, r_set)


    def test_participant_length(self):
        """Assert that participants equals the length of the input participants"""
        self.assertEqual(len(self.polyanna._participants), len(participants.keys()))


    def test_avg_failcount(self):
        """Find the failure rate of the selection algorithm."""
        total_fails = 0
        for drawing in range(1000):
            total_fails += polynanna.main().failcount
        print('Average Failcount: {}'.format(total_fails / 1000))



    @unittest.skip('Skip Restricted Set Printing')
    def test_print_all_restricted_set(self):
        """Print restricted sets for each participant"""
        for p in self.polyanna._participants:
            print(p.name, 'restricted_set:', p.restricted_set)

    @unittest.skip('Skip Results Printing')
    def test_print_results(self):
        """Print drawing results to the console."""
        for participant in self.polyanna._participants:
            print('{:<9} -->  {}'.format(participant.name, participant.giving_to))


class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Note this runs a drawing automatically."""
        self.polyanna = polynanna.main()
        seed_db.main()
        db = Database()
        db.bind(provider='sqlite', filename='participants.db')
        db.generate_mapping(create_tables=True)


    def tearDown(self):
        del self.polyanna

    @db_session
    def test_print_database(self):
        """Verify the database has only as many entries as the polyanna. Print the drawing results."""
        self.assertEqual(len(self.polyanna._participants), len(seed_db.Participant.select()),
                         msg='Number of Participants is not equal to the number of Database Entries')
        print('participants.db Results')
        print('{:<9} |||  {} \n'.format('Name', 'Giving To'))
        for p in seed_db.Participant.select():
            print('{:<9} -->  {} \n'.format(p.name, p.giving_to), end='')
        

if __name__ == '__main__':
    unittest.main()
