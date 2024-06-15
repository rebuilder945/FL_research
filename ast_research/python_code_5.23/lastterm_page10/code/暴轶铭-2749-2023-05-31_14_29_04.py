line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               line.append(s.upper(), end = ")          
        else:
               print(s.lower(), end='')
    else:
          line.append(s)


