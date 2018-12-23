class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 1:
            if len(nums) < 1:
                return -1 
            else:
                if nums[0] == target:
                    return 0
                else:
                    return -1 
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end: 
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
    
    
      