class Duck:
     def swim(self):
          print("I am A Duck and I Can Swim")
     def speaks(self):
          print("I Speaks Quak Quak")
     
class Dog:
     def swim(self):
          print("I am A dog I can Swim")
     def speaks(self):
          print("Bow Bow")
          
def display(duck):
     duck.swim()
     duck.speaks()
     print("Information Displayed")
     
duck=Duck()
dog=Dog()
display(dog)
     
     