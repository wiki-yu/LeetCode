class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums) < 2):
            return Flase
        buff_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in buff_dict:
                buff_dict[nums[i]] = i
            else:
                return [i, buff_dict[target - nums[i]]]
                