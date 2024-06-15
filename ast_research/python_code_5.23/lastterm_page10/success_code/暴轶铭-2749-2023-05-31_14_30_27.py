line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               line.add(s.upper())          
        else:
               print(s.lower(), end='')
    else:
          line.add(s)


