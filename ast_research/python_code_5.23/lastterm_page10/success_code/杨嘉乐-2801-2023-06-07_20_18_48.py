x=input()
stars=[0,0,0,0,0]
for i in x:
    if i.isdigit():
        stars[0]=1
    if ord("a")<=ord(i)<=ord("z"):
        stars[1]=1
    if ord("A")<=ord(i)<=ord("Z"):
        stars[2]=1
    if len(x)>=8:
        stars[3]=1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\" :
        stars[4]=1
print(sum(stars))
