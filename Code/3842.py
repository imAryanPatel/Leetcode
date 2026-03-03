class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        arr = []
        from collections import Counter
        freq = Counter(bulbs)
        for i in freq:
            if freq[i] % 2 != 0:
                arr.append(i)

        arr.sort()
        return arr

class Solution(object):
    def toggleLightBulbs(self, bulbs):
        e=set()
        for a in bulbs:
            if a in e:
                e.remove(a)
            else:
                e.add(a)
        return sorted(e)   