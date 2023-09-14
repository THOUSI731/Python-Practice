num=int(input("Enter Number of ROws: "))
for i in range(0,num):
     for j in range(num,i,-1):
          print(f"{j} ",end='')
     print()
     
# ===========================================
               # 5 4 3 2 1
               # 5 4 3 2
               # 5 4 3
               # 5 4
               # 5
# ================================================