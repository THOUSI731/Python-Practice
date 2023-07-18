status = int(input("Give us a status code: "))
match status:
     case 200:
          print("OK")
     case 201:
          print("Created")
     case 301:
          print("Moved Permanently")
     case 302:
          print("Found")
     case _:
          print("The status is unknown to us.")