a = input()
b = input()
color=['red','blue','yellow']
for i in color:
    if a not in color or b not in color:
        print("error")
if a=='red' and b=='blue' or b=='red' and a=='blue':
    print("purple")
if a=='red' and b=='yellow' or b=='red' and a=='yellow':
    print("orange")
if a=='yellow' and b=='blue' or b=='yellow' and a=='blue':
    print("green")
