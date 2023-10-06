import math
print()
class Solution:
    def majorityElement(self, nums: [1,2,3]):
         ele1=0
         ele2=0
         ele3=0
         count = math.floor(len(nums)/3)
         for i in nums:
              if ele1 !=0:
                   ele1 = nums[i]
                   if ele1 in nums > 1:
                        print(ele1)
               
         
         
         
         
a=Solution()
a.majorityElement()