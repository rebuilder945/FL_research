yuanlai = input().split()
a1,a2 = eval(input())
b1 = yuanlai[a1]
b2 = yuanlai[a2]
yuanlai[a1]=b2
yuanlai[a2]=b1
print(yuanlai)

