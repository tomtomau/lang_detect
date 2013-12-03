# Language detection
import unittest
import sys, re

class Detector:
	def __init__(self, dict_path):
		"""
		Constructor for detector object, takes in path to dictionary as argument
		"""
		self.dictionary = dict() #TODO: read file and parse into dictionary

		#Create dictionary of words with value being an array being language that word can originate from
		#EG {'Hello': [German, English]}

	def detect(self, text):
		"""
		Parse a text segment and respond with match percentage
		"""
		if text == "":
			raise BaseException("Text must be at least one letter long")
		score = 0
		wordset = re.findall(r"[\w']+", text)
		for word in wordset:
			if word in self.dictionary: # need to check case on the dictionary elements too
				score += 1

		return float(score)/len(wordset)

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
	#unittest.main()
