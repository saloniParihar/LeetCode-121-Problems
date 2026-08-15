class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
       """
        s = set()
        for i in range(0,len(nums)):
              if nums[i] not in s:
                     s.add(nums[i])
              else:
                   return True
        return False