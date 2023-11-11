# find the sum of two numbers that gets 10
list_=[6,5,4,3,9,8,0,1]
for i in range(len(list_)-1):
     for j in range(i+1,len(list_)):
          if list_[i] + list_[j] == 10:
               print([list_[i],list_[j]],'j')
               
# O(n2) - Time
# O(1) - Space


# Second Approad
list_2=[]
for i in range(len(list_)):
     num = list_[i]
     match = 10-num
     if match in list_2:
          print(num,match)
     else:
          list_2.append(num)
          
# O(n) - Space

