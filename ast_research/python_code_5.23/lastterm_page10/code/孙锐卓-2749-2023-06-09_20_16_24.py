line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               print(s.upper(),&#160;&#160;end='')          
        else:
               print(s.lower(), end='')
    else:
          print(s,&#160;&#160;end='')


