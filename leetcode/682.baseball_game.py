class Solution:
    def calPoints(self, operations) -> int:
        list_=operations 
        result = []
        for i,value in enumerate(list_):
            if value.isdigit() or value.startswith('-'):
                result.append(int(value))
            elif value == 'C':
                 result.pop()
            elif value == '+':
                 result.append(result[-2]+result[-1])
            elif value == 'D':
                 result.append(result[-1]*2)   
                 
        print(sum(result))

a=Solution()
a.calPoints(["5","-2","4","C","D","9","+","+"])