num = int(input("ENter Number Of Rows: "))
for i in range(1,num+1):
     for j in range(i,num+1):
          print(f"{j} ",end='')
     print()
     
# ===========================================
               # 1 2 3 4 5
               # 2 3 4 5
               # 3 4 5
               # 4 5
               # 5
# ===========================================