# Language detection
import unittest
import sys

class Detector:
	def __init__(self, dict_path):
		"""
		Constructor for detector object, takes in path to dictionary as argument
		"""
		self.dictionary = dict() #TODO: read file and parse into dictionary

	def detect(self, text):
		"""
		Parse a text segment and respond with match percentage
		"""
		score = 0
		# for each word
			# if word in dictionary
				# increase score

		# return percentage score

class TestDetector(unittest.TestCase):
	"""
	Unit testing object
	"""
	def setUp(self):
		# do nothing yet
		pass

	def test_(self):
		"""
		A test test, will build this up further when dictionary files can be read
		"""
		self.assertTrue(1==1)

if __name__ == '__main__':
	"""
	Incase this gets used elsewhere, then we don't want to run tests
	"""
	unittest.main()