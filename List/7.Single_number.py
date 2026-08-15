class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """for i in range(len(nums)):
             count = 0
             for j in range(len(nums)):  
                   if nums[i] == nums[j]: 
                          count += 1
             if count == 1:
                 return nums[i]"""

        ans = 0
        for i in range(0,len(nums)):
              ans = ans^nums[i]
        return ans
                        
