# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        

    def match(self, word_list):
        matches = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                matches.append(word)
        return matches


# How will you determine if one world is an anagram for another?
# You'll need to iterate over the list of words that the match() method takes an argument
# You will compare each word of that list to the word that the Anagram class is initialized with
# To determine one word is an anagram of another word, try determining if they are composed of the same letters. 
# You can use a list interpretation on a string to get a list of its individual letters
# You can compare two lists using the ==
# Two lists are equal if they contain the same elements, in the same order. Remeber that you can use sorted() on a list.