ls=[]
n = input() or 'p'
while (n!= 'p'):
    ls.append(n)
    n = input()
lst=[ls.count(x) for x in ls]
for i in ls:
    if ls.count(i)==max(lst):
        print('{} {}'.format(i,ls.count(i)))
