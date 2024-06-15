a=input()
d=0
for i in a:
    if i.isdigit():
        d+=1
        break
    if 'a'<=i<='x':
        d+=1
        break
    if 'A'<=i<='X':
        d+=1
        break
    if len(a)>=8:
        d+=1
        break
    if i in " ~!@#$%^&*()_=-/,.?<>;:[]{}|\ ":
        d+=1
        break
print(d)
