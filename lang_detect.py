# Language detection
import unittest
import sys, re

class Detector:
	def __init__(self, dict_path):
		"""
		Constructor for detector object, takes in path to dictionary as argument
		"""
		self.dictionary = dict() #TODO: read file and parse into dictionary

		# Create dictionary of words with value 0

		for line in reversed(open(dict_path).readlines()):
			if not line.startswith("%"):
				self.dictionary[line] = 1 # this is the first time we've seen this word


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
				self.dictionary[word] += 1 # let's count common words
				score += 1
				self.dictionary[word]+=1
		# return percentage score
		return float(score)/len(wordset)

	def resetWordCount(self, word):
		"""
		Reset occurence count of certain word in detector dictionary
		"""
		if word in self.dicionary:
			self.dictionary[word] = 0

	def resetAllWordCounts(self):
		"""
		Reset occurence counts of all words in detector dictionary
		"""
		for keys in self.dictionary:
			self.dictionary[keys] = 0


		# return percentage score
	def dictLength(self):
		"""
		Returns length of dictionary
		"""
		return len(self.dictionary)

	


class TestDetector(unittest.TestCase):
	"""
	Unit testing object
	"""
	def setUp(self):
		# do nothing yet
		pass

	def test_demo(self):
		"""
		A test test, will build this up further when dictionary files can be read
		"""
		self.assertTrue(1==1)

	def test_create_detector(self):
		"""
		A test to test reading of dictionary (Spanish)
		"""
		dict_path = 'de_neu.dic'
		SpanishDet = Detector(dict_path)
		Count = 0
		for line in open(dict_path).readlines():
			if not line.startswith("%"):
				Count+=1
		self.assertTrue(Count == SpanishDet.dictLength())

if __name__ == '__main__':
	"""
	Incase this gets used elsewhere, then we don't want to run tests
	"""
	unittest.main()
