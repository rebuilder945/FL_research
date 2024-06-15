a = input().split(',')
c,b = eval(input())
# try:
copy = a[c:c+1]
if c>len(a)+1 or c<-len(a):
    print('error')
for k in range(b):
    a.extend(copy)
for i in range(len(a)):
    a[i] = int(a[i])
print(a)
