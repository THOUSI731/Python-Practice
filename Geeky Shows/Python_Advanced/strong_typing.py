class Thousi:
     def walk(self):
          print("tHOUSI YOU CAN DO")
     
     
def myFunction(obj):
     if hasattr(obj,'walk'):
          obj.walk()
     else:
          print("SORRY dA")

t=Thousi()
myFunction(t)