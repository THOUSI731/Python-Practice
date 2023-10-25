import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=''.join([s for s in s if s.isalpha() or s.isalnum()][::-1]).lower()
        return True if  result == result[::-1]  else False
               
             
   
a=Solution()
print(a.isPalindrome("0P"))