class Solution(object):
    def sortByBits(self, arr):
        a = []
        for i in arr:
            p = bin(i)
            m = p.count('1')
            a.append([m,i])
            a.sort()
        r=[]
        for j in a:
            r.append(j[1])
        return r


        