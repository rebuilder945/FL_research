a = eval(input())
n = ''.join(a)
n = n.lower()
m = n
w = ''
for i in n:
    if i not in w:
        w += i + ','
s1 = w[:-1].split(',')

for i in s1:
    print(i,m.count(i),sep=',')



