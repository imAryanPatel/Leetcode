class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        from collections import Counter
        freq = Counter(arr)

        max_num = max(freq, key=freq.get)

        return max_num
class Solution(object):
    def findSpecialInteger(self, arr):
        
        n = len(arr)
        quarter = n // 4
        
        for i in range(n - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]       
            