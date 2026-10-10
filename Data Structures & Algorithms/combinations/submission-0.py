class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        self.helper(1, [], comb, n, k)
        return comb

    def helper(self, i, curComb, comb, n, k):
        if len(curComb) == k:
            comb.append(curComb.copy())
            return
        
        if i > n:
            return
        
        for j in range(i, n + 1):
            curComb.append(j)
            self.helper(j + 1, curComb, comb, n, k)
            curComb.pop()

            