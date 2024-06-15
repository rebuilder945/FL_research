line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               upper(s)          
        else:
               print(s.lower(), end='')
    else:
          continue


