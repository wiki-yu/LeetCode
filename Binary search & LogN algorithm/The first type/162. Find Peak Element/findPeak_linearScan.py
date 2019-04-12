class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            if i == 0:
                continue
            elif nums[i] > nums[i-1]:
                continue
            else:
                return i - 1
        return len(nums) - 1
