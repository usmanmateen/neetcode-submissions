class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i, x in enumerate(nums):
            if x not in seen:
                seen.add(x)
            else:
                return True
        return False
