num = int(input("Enter Number OF Rows: "))
for i in range(1,num+1):
     for j in range(i,0,-1):
          print(f"{j} ",end='')
     print()

# ==============================================
               # 1
               # 2 1
               # 3 2 1
               # 4 3 2 1
               # 5 4 3 2 1
# ===============================================