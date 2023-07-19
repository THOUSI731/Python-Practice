# =====================================================================================================================================================

a = [1, 342, 223, 'India', 'Fedora']
# a.append(45) # [1, 342, 223, 'India', 'Fedora', 45]
# a.insert(0,786) # [786, 1, 342, 223, 'India', 'Fedora']
# x = a.count(1); print(x) # 1
# a.remove(223) # [1, 342, 'India', 'Fedora']
# a.reverse() # ['Fedora', 'India', 223, 342, 1]
# b = ['45', '10' ,'20']; a.append(b) ;print(b) # [1, 342, 223, 'India', 'Fedora', ['45', '10', '20']] | b ['45', '10', '20'] will be -1 position
# b = ['45', '10' ,'20'] ; a.extend(b) ;  # [1, 342, 223, 'India', 'Fedora', '45', '10', '20'] See The Changes btw append and extend
# del a[-1] # [1, 342, 223, 'India']
# a.pop() # [1, 342, 223, 'India']
# a.pop(0) # [342, 223, 'India', 'Fedora'] 0th index removed

# =====================================================================================================================================================
# a = [1, 2, 3, 4, 0]
# print(sum(a)) # 10
# print(min(a)) # 1
# print(max(a)) # 4
# print(any(a)) # True
# print(all(a)) # True if there is string it will be false and the 0 case also


# =======================================================================================================================================================
# List Comprehension
# -----------------------------------
# a = [1,2,3]
# print([x ** 2 for x in a])
# -----------------------------------
# a = [1,2,3]
# print(list(x+1 for x in [x ** 2 for x in a]))
# ------------------------------------------------------------------------------------------------------------------
# for i, j in enumerate(['a', 'b', 'c'],start=1):
#       print(i, j)         # to loop through a list (or any sequence) and get iteration number at the same time
# ------------------------------------------------------------------------------------------------------------------
# a = ['Pradeepto', 'Kushal']
# b = ['OpenSUSE', 'Fedora']
# for x, y in zip(a, b):
#      print("%s uses %s" % (x, y))           # to iterate through two sequences same time
# -------------------------------------------------------------------------------------------------------------------