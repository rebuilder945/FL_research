line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               print(upper(s))          
        else:
               print(s.lower(), end='')
    else:
          print(s)


