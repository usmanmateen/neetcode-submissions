class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seen = {}

        for i, x in enumerate(nums):
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
        i = 0

        for color in [0, 1, 2]:
            for _ in range(seen.get(color, 0)):
                nums[i] = color
                i += 1
                    
