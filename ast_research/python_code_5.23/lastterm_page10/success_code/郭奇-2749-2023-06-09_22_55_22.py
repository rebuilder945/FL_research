line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               print(s.uuper(),end='')          
        else:
               print(s.lower(), end='')
    else:
          pass


