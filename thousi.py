list_=[1,1]
for i in range(1,10):
     list_.append(list_[i-1] + list_[i])
     
print(list_)