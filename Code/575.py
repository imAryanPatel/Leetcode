class Solution(object):
    def distributeCandies(self, candyType):
        if len(set(candyType)) <=1:
            return 1
        elif len(set(candyType)) < len(candyType)/2:
            return len(set(candyType))
        else:
            return len(candyType)/2
        
class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        m = len(set(candyType))
        t = min(n/2,m)
        return t