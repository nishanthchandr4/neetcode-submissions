class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []
        numbers = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

        def helper(curComb, digits):
            if not digits:
                res.append(curComb)
                return
            
            for c in numbers[digits[0]]:
                curComb += c
                helper(curComb, digits[1:])
                curComb = curComb[:-1]

        helper("", digits)
        return res

        