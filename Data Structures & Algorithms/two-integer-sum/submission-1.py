class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                t = nums[i] + nums[j]
                if target == t:
                    return [j, i]