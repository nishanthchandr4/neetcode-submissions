class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
    
        copy = nums[:]
        for num in copy:
            nums.append(num)
        return nums





        