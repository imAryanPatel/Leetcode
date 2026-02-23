class Solution(object):
    def minimumOperations(self, nums):
        seen = set()
        i = 0
        count = 0
        while i < len(nums):
            
            if nums[i] in seen:
                nums = nums[3:]
                seen.clear()
                
                count +=1
                i = 0
            else: 
                seen.add(nums[i])
                i+=1

        return count