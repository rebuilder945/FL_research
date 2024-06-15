line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               b.append(s.upper)          
        else:
               print(s.lower(), end='')
    else:
          b.append(s)


