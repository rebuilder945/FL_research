p = input().split()
n = list(map(int,p[1:]))
avg = sum(n)/3
n.sort(reverse=True)
print(p[0],end=' ')
for x in n:
    print('%.2f'%x,end=' ')
print('%.2f'%avg)
