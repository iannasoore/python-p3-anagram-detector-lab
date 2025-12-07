class Anagram:
	def __init__(self, word):
		self.word = word
		self._key = "".join(sorted(word.lower()))

	def match(self, candidates):
		"""Return list of words from `candidates` that are anagrams
		of the initialized word. Identical words (case-insensitive)
		are excluded.
		"""
		result = []
		for candidate in candidates:
			if candidate.lower() == self.word.lower():
				continue
			if "".join(sorted(candidate.lower())) == self._key:
				result.append(candidate)
		return result
