from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        freq = Counter(arr)
        count = []
        nums = set(arr)
        for i in nums:
            if freq[i] == i:
                count.append(i)
        if count == []:
            return -1
        else:
            return max(count)       