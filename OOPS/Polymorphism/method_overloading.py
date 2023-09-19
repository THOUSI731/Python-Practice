class A:
     def show(self):
          print("Welcome")
     def show(self,firstname=''):
          print("Welcome",firstname)
     def show(self,firstname='',lastname=''):
          print("Welcome",firstname,"your last name",lastname)
          

A=A()
A.show() # Welcome
A.show('yg')
A.show('yg','safiya')