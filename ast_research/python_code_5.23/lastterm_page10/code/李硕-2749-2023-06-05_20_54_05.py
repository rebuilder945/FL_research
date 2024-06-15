line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               print(s.upper(),end="”)          
        else:
               print(s.lower(), end='')
    else:
          print(s,end="")


