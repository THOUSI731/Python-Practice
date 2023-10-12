class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
               if char in bracket_pairs.values():
                    stack.append(char)
               elif char in bracket_pairs.keys():
                    if stack == [] or bracket_pairs[char] != stack.pop():
                         return False
               else:
                    return False

               return stack == []


a=Solution()
print(a.isValid("([])"))