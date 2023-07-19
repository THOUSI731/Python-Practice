# Q 1 : Take number of students as input
#   2 : Ask marks for three subjects as ‘Physics’, ‘Maths’,‘History’
#   3 : if the total marks for any student is less 120 then print he failed, or else say passed.

# Output :- 
# Enter the number of students:2
# Enter the name of the student 1: Babai
# Enter marks of Physics: 12
# Enter marks of Maths: 45
# Enter marks of History: 40
# Enter the name of the student 2: Tesla
# Enter marks of Physics: 99
# Enter marks of Maths: 98
# Enter marks of History: 99
# Babai 's total marks 97
# Babai failed :(
# Tesla 's total marks 296
# Tesla passed :)

n = int(input("Enter the number of students:"))
data = {} # here we will store the student data
languages = ('Physics', 'Maths', 'History') 
for i in range(n): 
     name = input('Enter the name of the student %d: ' % (i + 1)) #Get the name of students
     marks = []
     for x in languages:
          marks.append(int(input('Enter marks of %s: ' % x))) #Get the marks for
     data[name] = marks
for x, y in data.items():
     total = sum(y)
     print("%s 's total marks %d" % (x, total))
     if total < 120:
          print("%s failed :(" % x)
     else:
          print("%s passed :)" % x)
     