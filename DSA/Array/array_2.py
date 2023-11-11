# Move all specifiedt target to right

list_=[6,1,6,8,10,4,15,6,3,9,6]
for i in range(len(list_)-1):
     for j in range(i+1,len(list_)):
          if list_[i] == 3:
               temp=list_[i]
               list_[i] = list_[j]
               list_[j] = temp
print(list_)
               
for i in range(len(list_)):
     if list_[i] == 6:
          temp = list_[i]
               