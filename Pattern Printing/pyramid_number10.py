num=int(input("Enter Number of Rows: "))
for i in range(num,0,-1):
     for j in range(i,0,-1):
          print(f"{j} ",end='')
     print()
     
# ========================================
               # 5 4 3 2 1
               # 4 3 2 1
               # 3 2 1
               # 2 1
               # 1
# ==========================================