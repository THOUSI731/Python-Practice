class Solution:
    def reverseWords(self, s: str) -> str:
        list_=s.split(' ')
        result=''
        for i in list_:
             result=result + i[::-1] + " "
        print(result)
             
        

a=Solution()
a.reverseWords("Let's take LeetCode contest")