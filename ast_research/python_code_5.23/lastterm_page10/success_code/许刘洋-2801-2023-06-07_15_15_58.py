a=input()
d=0
for i in a:
    if i.isdigit():
        d+=1
    if 'a'<=i<='x':
        d+=1
    if 'A'<=i<='X':
        d+=1
    if len(a)>=8:
        d+=1
    if i in " ~!@#$%^&*()_=-/,.?<>;:[]{}|\ ":
        d+=1
print(d)
