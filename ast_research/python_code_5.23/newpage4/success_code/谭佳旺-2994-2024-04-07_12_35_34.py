lis1 =list(eval(input()))
a,b =input().split(',')
a=int(a)
b=int(b)
if a<len(lis1):
    for i in range(b):
        lis2=lis1[a]
        lis1.append(lis2)
    print(lis1)
if a>len(lis1):
    print('error')

