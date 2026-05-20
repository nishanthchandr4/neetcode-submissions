class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
    
        copy = nums.copy()

        for num in copy:
            nums.append(num)
        return nums





        