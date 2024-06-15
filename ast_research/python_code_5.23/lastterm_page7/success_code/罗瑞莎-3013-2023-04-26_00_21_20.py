GDP = {}
s = input()
while s!='ok':
    c,n = s.split(' ')
    GDP[c] = n
    s = input()
c1 = list(GDP.keys())
n1 = list(GDP.values())
c1.sort()
n1.sort()
lst = list(map(int,n1))
print(c1)
print(lst)
print("yes" if 'India' in c1 else "no")
print(sum(lst))
