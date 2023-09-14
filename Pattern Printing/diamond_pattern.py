num = int(input("Number of Rows For Your Diamond Pattern: "))
for i in range(1,num+1):
     for space in range(i,num):
          print(" ",end='')
     for star in range(i):
          print("* ",end='')
     print()
     if i==num:
          for i in range(0,num):
               if i==0:
                    continue
               for space in range(i):
                    print(" ",end='')
               for star in range(i,num):
                    print("* ",end='')
               print()
               
# =========================================================
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# ==========================================================