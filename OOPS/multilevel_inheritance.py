class Human:
     pass

class Boy(Human):
     pass

class Men(Boy):
     pass

class Warrior(Men):
     pass

class Protector(Warrior):
     pass

print()

hi=Protector()
print(hi.mro())