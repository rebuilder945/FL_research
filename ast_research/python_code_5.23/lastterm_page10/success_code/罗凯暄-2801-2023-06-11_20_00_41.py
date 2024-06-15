n=input()
level=0
lst=list(n)
if len(lst)>=8:
    level+=1
for x in lst:
    if 'a'<=x<='z':
        level+=1
        break
for x in lst:
    if 'A'<=x<='Z':
        level+=1
        break
for x in lst:
    if '0'<=x<='9':
        level+=1
        break
for x in lst:
    if x in '~!#$%^&*()_=-/,.?<>:;[]{}|':
        level+=1
        break
print(level)

