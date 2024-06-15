line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               s.append(s.upper)          
        else:
               print(s.lower(), end='')
    else:
          line.append(s)


