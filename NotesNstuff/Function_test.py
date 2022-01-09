import unittest
from AfunctionFortesting import rearange_name

class TestRearrange(unittest.TestCase):
	def test_basic(self): # Any "test" methods must have names starting with the "test" prefix
		testcase = "Snake, Solid"
		expected = "full name: Solid Snake"
		self.assertEqual(rearange_name(testcase), expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearange_name(testcase), expected)	

unittest.main()