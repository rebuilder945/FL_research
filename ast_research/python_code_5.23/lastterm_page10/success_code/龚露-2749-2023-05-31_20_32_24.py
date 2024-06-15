line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               s.upper()          
        else:
               print(s.lower(), end='')
    else:
          s=s


