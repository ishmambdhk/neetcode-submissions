
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 1. Use a dictionary instead of set()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:  # 2. Indent inside the for loop (12 spaces)
                return [seen[diff], i]
            seen[num] = i  # 2. Indent inside the for loop (12 spaces)

        return []  # 3. Indent inside twoSum method (8 spaces)