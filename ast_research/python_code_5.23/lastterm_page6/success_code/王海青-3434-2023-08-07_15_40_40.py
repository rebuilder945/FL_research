a=input()
b=input()
if a=='red' and b=='blue':
    print("purple")
elif a=='red' and b=='yellow':
    print("orange")
elif a=='yellow' and b=='blue':
    print("green")
elif  a not in ('red','blue','yellow') or b not in ('red','blue','yellow') or a==b:
    print("error")
