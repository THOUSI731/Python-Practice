def rotate(nums, k) -> None:
     """
     Do not return anything, modify nums in-place instead.
     """
     for i in range(k):
          var_=nums.pop()
          nums.insert(0,var_)
     return nums
        
            
print(rotate([1,2,3,4,5,6,7],3))
