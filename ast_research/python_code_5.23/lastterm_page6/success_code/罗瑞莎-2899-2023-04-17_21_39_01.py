n,m = input().split(' ')
n = eval(n)
m = eval(m)
flag = 0
lst = []
for i in range(n,m):
    lst.append(i)
a = lst[0]*100+lst[1]*10+lst[2]
b = lst[0]*100+lst[1]+lst[2]*10
c = lst[0]*10+lst[1]+lst[2]*100
d = lst[0]+lst[1]*10+lst[2]*100
e = lst[0]+lst[1]*100+lst[2]*10
f = lst[0]*10+lst[1]*100+lst[2]
for j in 'abcdef':
    if eval(j)>100:
        print(eval(j))
        flag = 1
if flag == 0:
    print("illegal input")

print(a)    
