class Solution:
    def isValid(self, s: str) -> bool:
        
        arr = {')':'(', ']':'[', '}':'{'}
        stack = []

        for str in s:
            if str in arr:
               if stack and stack[-1] == arr[str]:
                    stack.pop()
               else:
                    return False
            else:
                stack.append(str)
        return not stack


