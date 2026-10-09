class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSet, curSet = [], []
        self.helper(0, nums, subSet, curSet)
        return subSet

    def helper(self, i, nums, subSet, curSet):
        if i >= len(nums):
            subSet.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i + 1, nums, subSet, curSet)
        curSet.pop()

        self.helper(i + 1, nums, subSet, curSet)
        

        