class Solution:
    def thousandSeparator(self, n: int) -> str:
          length=0
          for i in str(n):
               length+=1
          ans=str(n)   
          if length==3:
               return ans
          str_=''
          for i in range(1,length+1):
               if i % 3==0:
                    if i == length:
                         str_= ans[-i]+str_
                         break
                    str_= "."+ans[-i]+str_
                    continue
               str_ =  ans[-i] + str_
          return str_

   
a=Solution()
print(a.thousandSeparator(600000))