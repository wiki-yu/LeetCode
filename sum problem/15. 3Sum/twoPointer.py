class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
    
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]: #prevent the same value
                continue
            target = - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] < target:
                     start = start + 1
                elif nums[start] + nums[end] > target:
                     end = end - 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start+1] == nums[start]:
                        start += 1
                    while start < end and nums[end-1] == nums[end]:
                        end -= 1
                    start = start + 1
                    end = end -1      
        return result
                
                
        
