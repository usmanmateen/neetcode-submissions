class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        majority = len(nums)/2
        for i, x in enumerate(nums):
            if x not in seen:
               seen[x] = 1
            else:
                seen[x] +=1
        for key in seen:
            if seen[key] > majority:
                return key