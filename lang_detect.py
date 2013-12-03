# Language detection

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