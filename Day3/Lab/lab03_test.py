import unittest

from lab03 import * # needs to be same wd as lab03.py

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
        self.assertEqual(shout("shout"),"SHOUT")
        self.assertTrue(type(shout("shout")) == str)
        with self.assertRaises(TypeError):
            shout(["Loud", "and", "clear"])

    def test_reverse(self):
        self.assertEqual(reverse("shout"),"tuohs")
        self.assertTrue(type(reverse("shout")) == str)
        with self.assertRaises(TypeError):
            reverse(["Loud", "and", "clear"])

    def test_reversewords(self):
        self.assertEqual(reversewords("shout loud and clear"),"clear and loud shout")
        self.assertTrue(type(reversewords("shout loud and clear")) == str)
        with self.assertRaises(TypeError):
            reversewords(["Loud", "and", "clear"])

    def test_reversewordletters(self):
        self.assertEqual(reversewordletters("shout loud and clear"),"tuohs duol dna raelc")
        self.assertTrue(type(reversewordletters("shout loud and clear")) == str)
        with self.assertRaises(TypeError):
            reversewordletters(["Loud", "and", "clear"])
            
            
    #def test_piglatin(self):


if __name__ == '__main__':
  unittest.main()

