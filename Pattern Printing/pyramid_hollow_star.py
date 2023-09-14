num = int(input("Enter Number Of Rows: "))
for i in range(num):
     for j in range(i+1):
          if i == 0 or i == num-1 or j == 0 or j==i:
               print("* ",end='')
          else:
               print("  ",end='')
     print() 

# ===========================================================
                    # *
                    # * *
                    # *   *
                    # *     *
                    # * * * * *
#===============================================================