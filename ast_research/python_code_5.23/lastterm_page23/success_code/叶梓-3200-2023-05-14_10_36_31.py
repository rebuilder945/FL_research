line = input()
for s in line():
    if s.islower():
        print(s.upper(),end="")          
    else:
        print(s,end='')
