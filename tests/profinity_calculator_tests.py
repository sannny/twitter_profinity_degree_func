import unittest

import profiniy_calculator


class MyTestCase(unittest.TestCase):

    def test_read_csv_empty_path(self):
        #empty path should return empty list
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.read_csv(''), [])

    def test_read_csv_null_path(self):
        #null path should return empty list
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.read_csv(None), [])

    def test_profin_calculator_null(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.profin_calculator(None), 0)

    def test_profin_calculator_empty(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.profin_calculator([]), 0)

    def test_profin_calculator(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.profin_calculator([["@mrmak", "I hate these X's"]]), [1])

    def test_pattern_matching_empty_word(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = (), index = 0, sentence = "I hate these X's"), 0)

    def test_pattern_matching_null_word(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = None, index = 0, sentence = "I hate these X's"), 0)

    def test_pattern_matching_null_index(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = ('hate', 'X'), index = None, sentence = "I hate these X's"), 0)

    def test_pattern_matching_wrong_index(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = ('hate', 'X'), index = '1abc', sentence = "I hate these X's"), 0)

    def test_pattern_matching_empty_sentence(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = ('hate', 'X'), index = 0, sentence = ""), 0)

    def test_pattern_matching_null_sentence(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = ('hate', 'X'), index = 0, sentence = None), 0)

    def test_pattern_matching(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.pattern_matching(words = ('hate', 'X'), index = 0, sentence = "I hate these X's"), 1)

    def test_profin_ranker(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.profin_ranker(scores = [1, 2, 3]), ['Low', 'Moderate', 'Extreme'])

    def test_profin_ranker_empty(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.profin_ranker(scores = []), [])

    def test_profin_ranker_null(self):
        racial_slurs = {
            ('hate', 'X'): 1,
            ('Y', 'back', 'country'): 2,
            ('D', 'love', 'E'): 1.5,
            ('M', 'G', 'love'): 1,
            ('X', 'go', 'C'): 2.5
        }
        pc = profiniy_calculator.Profinity_calculator(racial_slurs)
        self.assertEqual(pc.profin_ranker(scores = None), [])




if __name__ == '__main__':
    unittest.main()
