a  = list(eval(input()))
n,m=eval(input())
b = a[n]
if n>=len(a) or n<(-len(a)):
    print('error')
else:
    for i in range(m):
        a.append(b)
    print(a)
