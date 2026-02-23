class Solution(object):
    def reverseWords(self, s):
        word = list(s)
        word = s.split()
        word.reverse()
        return " ".join(word)