class Solution:
    def sumOfUnique(self, nums) -> int:
        result=[x for x in nums if nums.count(x)==1]
        return sum(result)
   
   
a=Solution()
print(a.sumOfUnique([1,2,3,4,5]))