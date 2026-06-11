class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b={}
        for i in range (0,len(nums)):
            if target-nums[i] in b:
                return [b[target-nums[i]], i]
            b[nums[i]]=i
