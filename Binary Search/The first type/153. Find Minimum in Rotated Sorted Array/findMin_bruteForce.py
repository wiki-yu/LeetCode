class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
     
        start, end = 0, len(nums) - 1
        
        if nums[end] < nums[start]:
            for i in range(len(nums)):
                if i == 0:
                    continue
                elif i != 0 and nums[i] > nums[i-1]:
                    continue
                else:
                    return nums[i]
        else:
            return nums[start]
