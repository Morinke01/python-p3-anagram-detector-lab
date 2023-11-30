class Anagram:
    def __init__(self, word) -> None:
        self.word = word

    def is_anagram(self, word2):
        return sorted(self.word) == sorted(word2)

    def match(self, candidate_list):
        correct_anagrams = [candidate for candidate in candidate_list if self.is_anagram(candidate)]
        if correct_anagrams:
            print(f"The correct anagram(s) for '{self.word}' is/are: {correct_anagrams}")
        else:
            return []
        return correct_anagrams
