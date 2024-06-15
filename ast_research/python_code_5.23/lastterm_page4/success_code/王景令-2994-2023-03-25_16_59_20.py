a = input().split(',')
b,c = eval(input())
if -len(a) <= b <= len(a)-1:
    for i in range(c):
        a.append(c[b])
    print(a)
else:
    print('error')
