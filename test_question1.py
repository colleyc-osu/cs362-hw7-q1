import unittest
import question1

class TestCase(unittest.TestCase):

	def test1(self):
		self.assertEqual(question1.fizzbuzz(2), "1	2")


if __name__ == '__main__':
	unittest.main()