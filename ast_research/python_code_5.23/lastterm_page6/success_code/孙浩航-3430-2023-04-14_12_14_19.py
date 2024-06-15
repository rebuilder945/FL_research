a=int(input())
yuefeng={1,2,3,4,5,6,7,8,9,10,11,12}
c={3,4,5}
x={6,7,8}
q={9,10,11}

if not a in yuefeng:
    print("error")
elif a in c:
    print("spring")
elif a in x:
    print("summer")
elif a in q:
    print("autumn")
else:
    print("winter")
