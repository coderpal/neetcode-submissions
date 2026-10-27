class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if the length is equal, if not, then it is not anagram
        if len(s) != len(t):
            return False

        # initialize empty dictionary
        # we will add the count of each character to ascertain anagram
        count_s = {}
        count_t = {}

        # now, we will count each character and add it to our initialized dictionary
        for char_s, char_t in zip(s, t): # zip lets us lookup simultaneously
            count_s[char_s] = count_s.get(char_s, 0) + 1
            count_t[char_t] = count_t.get(char_t, 0) + 1

        return count_s == count_t
        