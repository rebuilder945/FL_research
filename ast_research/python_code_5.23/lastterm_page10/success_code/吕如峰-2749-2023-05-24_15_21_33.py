line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               s.append(n.upper())          
        else:
               print(s.lower(), end='')
    else:
          s.append(n.lower())


