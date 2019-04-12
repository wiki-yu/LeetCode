class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        arr = []
        
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                start, end = j + 1, len(nums) - 1
                while start < end:     
                    sums = nums[i] + nums[j] + nums[start] + nums[end]
                    if sums < target:
                        start += 1
                    elif sums > target:
                        end -= 1
                    else:
                        arr.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]: 
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1   
        return arr
                
