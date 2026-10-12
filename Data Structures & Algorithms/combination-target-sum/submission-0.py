class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        self.helper([], comb, nums, target)
        return comb

    def helper(self, curComb, comb, nums, target):
        if (sum(curComb) == target):
            comb.append(curComb.copy())
            return 
        if sum(curComb) > target:
            return
        
        for i in range(len(nums)):
            curComb.append(nums[i])
            self.helper(curComb, comb, nums[i:], target)
            curComb.pop()

        

        
    
