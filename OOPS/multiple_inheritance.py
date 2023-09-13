class Male:
     def __init__(self):
          self.num_eyes = 2
          self.num_nose = 1

     def eat(self):
          print("I can eat")
          
          
class Female:
     def __init__(self,name):
          self.name = name
          
     def smile(self):
          print("I can Smile")


class Boy(Male,Female):
     def __init__(self):
          pass

male=Boy()
print(male.eat())
print(male.smile())
