class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
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

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, subSet, curSet)



        