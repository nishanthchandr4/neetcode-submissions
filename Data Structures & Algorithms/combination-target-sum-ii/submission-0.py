class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(i, curComb, total):

            if total == target:
                res.append(curComb.copy())
                return

            if i >= len(candidates) or total > target:
                return

            curComb.append(candidates[i])
            helper(i + 1, curComb, total + candidates[i])
            curComb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            helper(i + 1, curComb, total)
        
        helper(0, [], 0)
        return res



        
        
        
            