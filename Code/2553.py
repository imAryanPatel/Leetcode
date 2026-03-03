class Solution(object):
    def separateDigits(self, nums):
        n= []
        for i in nums:
            for j in str(i):
                n.append(int(j))
        return n


class Solution(object):
    def separateDigits(self, nums):
        result= []
        for i in nums:
            temp =[]
            while i>0:
                temp.append(i%10)
                i= i//10
            result.extend(temp[::-1])
        return result