str1 = input()
li1 = list(map(int, str1.split(',')))
n,m=map(int,input().split(','))
if n>=len(li1):
    print('error')

else:
    c1=li1[n]
    for j in range(m):
        li1+=[c1]
    print(li1)

