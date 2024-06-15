a = list(input().split(','))
n,m = int(input())
if n<len(a):
    print('error')
else:
   b = a[n]
   a.append(b)**m
print(a)

