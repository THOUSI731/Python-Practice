class A:
     def show(self):
          print("THis is parent class method")

class B(A):
     def show(self):
          super().show()
          print("This is child class Method")
          
          
b=B()
b.show()