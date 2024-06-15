yuanlai = input().split()
xulie = input().split()
a1 = xulie[0]
a2 = xulie[1]
b1 = yuanlai[a1]
b2 = yuanlai[a2]
yuanlai[a1]=b2
yuanlai[a2]=b1
print(yuanlai)

