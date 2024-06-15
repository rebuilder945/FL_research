a=str(input())
b=str(input())
list1=['red','blue','yellow']
if a!=b and a in list1 and b in list1:
    if (a=='red' and b=='blue') or (a=='blue' and b=='red'):
        print("purple")
    elif(a=='red' and b=='yellow') or (a=='yellow' and b=='red'):
        print("orange")
    elif(a=='yellow' and b=='blue') or (a=='blue' and b=='yellow'):
        print("green")
else:
    print("error")
