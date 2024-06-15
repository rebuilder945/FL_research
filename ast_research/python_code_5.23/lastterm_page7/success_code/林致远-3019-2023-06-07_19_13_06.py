s = input().split()
g = list(map(int,s[1:]))
g.sort(reverse=True)
print(s[0],end=' ')
for x in g:
    print('%.2f' % x,end=' ')
n = sum(g)/len(g)
print('%.2f' % n)
