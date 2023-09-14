num = int(input("Enter Number of Rows: "))
for i in range(1,num+1):
     for space in range(num,i,-1):
          print(" ",end='')
     for star in range(1,i*2):
          print("*",end='')
     print()
     
# ===========================================
#     *
#    ***
#   *****
#  *******
# *********
# =============================================