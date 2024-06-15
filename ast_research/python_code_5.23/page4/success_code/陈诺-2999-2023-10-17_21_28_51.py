import copy
a = list(map(str,input().split()))
b,c = map(int,input(),split())
d = copy.deepcopy(a)
d[b]=a[c]
d[c]=a[b]
print(d)
