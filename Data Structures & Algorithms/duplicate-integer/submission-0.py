class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set(nums)
        q = len(nums)

        if len(nums1) < q:
            return True
        else:
            return False