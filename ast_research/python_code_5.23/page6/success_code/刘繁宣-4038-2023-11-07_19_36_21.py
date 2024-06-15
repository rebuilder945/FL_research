s=''.join(input())
n1,n2,n3,n4=0,0,0,0
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in s:
        n1 += s.count(i)
for i in range(10):
    if str(i) in s:
        n2 += s.count(str(i))
for i in s:
    if i in [' ']:
        n3+=1
n4=len(s)-n1-n2-n3
print(n1,n3,n2,n4)
