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
            while start + 1 < end:
                mid = (start + end) / 2
                if nums[mid] > nums[0]:
                    start = mid
                else:
                    end = mid
            if nums[start] > nums[end]:
                return nums[end]
            else:
                return nums[start]       
        else:
            return nums[start]
