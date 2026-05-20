class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}

        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            elif i in numbers:
                return True
        return False