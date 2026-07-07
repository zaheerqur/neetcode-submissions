class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) ## [1,2,3,3] -> len(set(nums)) = 3, len(nums) = 4