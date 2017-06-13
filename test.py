import unittest
import polynanna


class TestPolynanna(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.polyanna = polynanna.main()

    def tearDown(self):
        print('In tearDown()')
        del self.polyanna

    def test_drawing_validity(self):
        print('in test()')
        for p in self.polyanna.participants:
            with self.subTest(p=p):
                self.assertNotIn(p.giving_to, p.restricted_set)


if __name__ == '__main__':
    unittest.main()
