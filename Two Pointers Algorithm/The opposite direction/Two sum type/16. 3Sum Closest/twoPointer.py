class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = 1000
        val = 0
        
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            
            while start < end:
                sums = nums[i] + nums[start] + nums[end]
                if abs(sums - target) < diff:
                    diff = abs(sums - target)
                    val = sums
                
                if sums > target:
                    end -= 1
                elif sums < target:
                    start += 1
                else:
                    return target
        return val             
        
        
        
       
        
