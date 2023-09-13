class University:
     def __init__(self,uni_name):
          self.university_name=uni_name
          
     def show_details(self):
          print(f"University Name :  {self.university_name}")
          

class Course(University):
     def __init__(self, course_name,uni_name):
          super().__init__(uni_name)
          self.course_name = course_name
          
     def show_details(self):
          super().show_details()
          print(f"Course Name: {self.course_name}")

class Branch(University):
     def __init__(self, uni_name,branch_name):
          super().__init__(uni_name)
          self.branch_name = branch_name
     
     def show_details(self):
          super().show_details()
          print(f"Branch Name: {self.branch_name}")

class Student(Branch):
     def __init__(self, uni_name, branch_name,student_name):
          super().__init__(uni_name, branch_name)
          self.student_name= student_name
     
     def show_details(self):
          super().show_details()
          print(f"Student Name: {self.student_name}")

class Faculty(Branch):
     def __init__(self, uni_name, branch_name,faculty_name):
          super().__init__(uni_name, branch_name)
          self.faculty_name= faculty_name
     
     def show_details(self):
          super().show_details()
          print(f"Faculty Name: {self.faculty_name}")

# u=University("Bridgeon")
# u.show_details()

# c=Course("Python","Bridgeon")
# c.show_details()

# b=Branch("Bridgeon","Shaheen")
# b.show_details()

# s=Student("Bridgeon","Shaheen","Thouseef")
# s.show_details()

f=Faculty("Bridgeon","Shaheen","Kozhippuram Hub")
f.show_details()

