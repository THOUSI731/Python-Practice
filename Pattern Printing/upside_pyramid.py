num=int(input("Enter Number of Rows: "))
for i in range(num,0,-1):
     for space in range(i,num):
          print(" ",end='')
          
     for star in range(0,i):
          print("* ",end='')
     print()
          
# =================================================
     # * * * * *
     #  * * * *
     #   * * *
     #    * *
     #     *
# =================================================