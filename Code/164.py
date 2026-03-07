class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        maxcount = 0
        if len(nums) < 2:
            return 0
        for i in range(len(nums)-1):
            count = nums[i+1] - nums[i]
            maxcount = max(maxcount,count)
        return maxcount
        