class Solution(object):
    def minPartitions(self, n):
        digit = max(n)
        return int(digit)


class Solution(object):
    def minPartitions(self, n):
        for i in range(9,-1,-1):
            if str(i) in n:
                return i
        