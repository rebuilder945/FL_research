line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               print(s.upper(), sep='')          
        else:
               print(s.lower(), end='')
    else:
          print(s)


