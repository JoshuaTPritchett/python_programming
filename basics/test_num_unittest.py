import unittest
from number import convert_binary

class TestNum(unittest.TestCase):

		def setUp(self):
				pass

		def test_binary(self):
				self.assertEqual(convert_binary(8), '1000')



if __name__ == '__main__':
	unittest.main()
