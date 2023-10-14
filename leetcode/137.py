
from collections import Counter

def singleNumber(nums) -> int:
     count=Counter(nums)
     for value,key in count.items():
          if key==1:
               return value



print(singleNumber([2,2,3,2]))