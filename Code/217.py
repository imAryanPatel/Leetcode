def containsDuplicate(self, nums):
        nums.sort()
        if len(nums)>1:
            for i in range(len(nums)):
                if nums[i] == nums[i-1]:
                    return True
            return False
        else:
            return False
         

def containsDuplicate(self, nums):
    n = len(nums)
    seen = set()
    for i in range(n):
          if nums[i] in seen:
               return True
          else:
               seen.add(nums[i])
    return False