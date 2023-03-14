import re
import unittest
import os
import csv

def get_profs(filepath):
    """
    This function accepts a CSV file, filepath, and parses it to return a list of
    lists. Each list should contain the name, title(s), and email addrress of professors
    at UMSI. This should only contain professors, not lecturers or research fellows.
    """
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filepath)
    pass

def get_valid_emails(prof_list):
    """
    This function accepts a list of lists and returns a dictionary. The keys should be
    the names of professors with valid email addresses and the values should be the email
    addresses of the professors. A valid email address should just have lowercase alphabetic
    characters and end with @umich.edu.
    Examples of invalid email addresses:
        buisl@umich.edu.com
        mjguz@um1ch.edu
        ajflynn @umich.edu
        vgvinodv@umich_.edu
    """
    pass



class TestDiscussion9(unittest.TestCase):
    def setUp(self):
        self.prof_list = [
            ['Patricia Abbott', 'Adjunct Clinical Associate Professor of Information, School of Information', 'pabbott@umich.edu'],
            ['Mark Ackerman', 'George Herbert Mead Collegiate Professor of Human-Computer Interaction, Professor of Information, School of Information, Professor of Electrical Engineering and Computer Science, College of Engineering and Professor of Learning Health Sciences, Medical School', 'ackerm@umich.edu'],
            ['Eytan Adar', 'Associate Professor of Information, School of Information and Associate Professor of Electrical Engineering and Computer Science, College of Engineering', 'eadar@umich.edu'],
        ]

    def test_get_profs(self):
        profs = get_profs('umsi_faculty.csv')
        self.assertIsInstance(profs, list)
        self.assertIsInstance(profs[0], list)
        self.assertEqual(len(profs), 102)
        self.assertEqual(profs[:3], self.prof_list)

    def test_get_valid_emails(self):
        profs = get_profs('umsi_faculty.csv')
        valid_emails_dict = get_valid_emails(profs)
        self.assertIsInstance(valid_emails_dict, dict)
        self.assertEqual(len(valid_emails_dict), 90)




if __name__ == '__main__':
    unittest.main(verbosity=2)