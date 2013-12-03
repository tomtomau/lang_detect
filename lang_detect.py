# Language detection
import unittest
import sys, re

class Detector:
	def __init__(self, language, dict_path):
		"""
		Constructor for detector object, takes in path to dictionary as argument
		"""
		self.language = language
		self.dictionary = dict() #TODO: read file and parse into dictionary

		# Create dictionary of words with value 0
		for line in open(dict_path).readlines():
			if not "%" in line:
				key = line.lower().strip() # lower case and remove \n
				if not key in self.dictionary:
					self.dictionary[key] = 0 # this is the first time we've seen this word
		

	def detect(self, text):
		"""
		Parse a text segment and respond with match percentage
		"""
		if text == "":
			raise BaseException("Text must be at least one letter long")
		score = 0
		wordset = re.findall(r"[\w']+", text)
		for word in wordset:
			lower_word = word.lower()
			if lower_word in self.dictionary: # need to check case on the dictionary elements too
				self.dictionary[lower_word] += 1 # let's count common words
				score += 1
				self.dictionary[lower_word]+=1
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
		dict_path = 'tests/test_construction.dic'
		language_name = "Hitchhiker"
		hitchhiker = Detector(language_name, dict_path)
		
		self.assertTrue(hitchhiker.dictLength() == 8)
		self.assertTrue(hitchhiker.language == language_name)

if __name__ == '__main__':
	"""
	Incase this gets used elsewhere, then we don't want to run tests
	"""
	test_text = open("tests/test_text.txt").read()
	languages = [["German", "de_neu.dic"], ["English", "eng_com.dic"]]
	detectors = list()
	for language in languages:
		detectors.append(Detector(language[0], language[1]))

	for detector in detectors:
		print detector.language + ", " + str(detector.detect(test_text))

	# And run the tests
	unittest.main()