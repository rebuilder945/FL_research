line = input()
for s in line:
    if s.isalpha():
        if s.islower():
               s=s.upper()          
        else:
               print(s.lower(), end='')
    else:
          print(s,end="")


