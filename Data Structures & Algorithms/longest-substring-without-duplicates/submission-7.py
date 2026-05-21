class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        word = set()
        maxLength = 0

        for r in range(len(s)):
            while s[r] in word:
                word.remove(s[l])
                l += 1
            word.add(s[r])
            maxLength = max(len(word), maxLength)
        return maxLength


