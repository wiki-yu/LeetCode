class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        if nums[start] > target:
            return start 
        elif nums[end] < target:
            return end 
        else:
            return start + 1
            
        
          
