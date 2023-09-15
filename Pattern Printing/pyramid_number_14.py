num= int(input("Enter Number Of Rows: "))
for i in range(1,num+1):
     for j in range(1,i+1):
          print(f"{j}",end='')
     print()
     if i==num:
          for i in range(num-1,0,-1):
               for j in range(1,i+1):
                    print(f"{j}",end='')
               print()

# ===================================================
                    # 1
                    # 12
                    # 123
                    # 1234
                    # 12345
                    # 1234
                    # 123
                    # 12
                    # 1
# ====================================================