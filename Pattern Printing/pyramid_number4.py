num = int(input("Enter Number of Rows: "))
for i in range(num,-1,-1):
     for j in range(num,i,-1):
          print(f"{j} ",end='')
     print()
     
# ============================================
               # 5
               # 5 4
               # 5 4 3
               # 5 4 3 2
               # 5 4 3 2 1
#==============================================