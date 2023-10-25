class Solution:
    def reverseWords(self, s: str) -> str:
          a=s.strip().split()
          result=''
          for i in range(1,len(a)+1):
               result = result+a[-i] + " "
          print(result)
   
   
a=Solution()
a.reverseWords("the sky is blue")
