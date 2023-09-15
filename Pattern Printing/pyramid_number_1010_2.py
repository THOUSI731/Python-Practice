num = int(input("Enter Number Of Rows: "))
k=1
for i in range(1,num+1):
     for j in range(i):
          if k%2==0:    
               print("0 ",end='')
          else:
               print("1 ",end='')
          k+=1
     print()
          
# ================================================
                    # 1
                    # 0 1
                    # 0 1 0
                    # 1 0 1 0
                    # 1 0 1 0 1
# =================================================