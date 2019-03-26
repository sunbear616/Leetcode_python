class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) < 2:
            pass
        r = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in r:
                return [i, nums.index(comp)]
            r.append(nums[i])
