num=int(input("Enter Number Of Rows: "))
for i in range(1,num+1):
     for space in range(num,i,-1):
          print(" ",end='')
     for star in range(1,i+1):
          print(f"{star}",end='')
     print()

# ===============================================
                    #     1
                    #    12
                    #   123
                    #  1234
                    # 12345
# ===============================================