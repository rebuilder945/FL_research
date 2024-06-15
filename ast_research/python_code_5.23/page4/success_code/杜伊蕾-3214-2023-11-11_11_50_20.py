'''a=input().split(',')
a=list(a)
b=eval(input())
m=[]
for x in range(a):
    n=[]
    n.append(a[x])
    n.append(b[x])
    m.append(n)
print(m)'''

'''n,m,l=map(int,input().split(','))
c=[]
for i in range (m):
    d=n+l*i
    c.append(d)
print(c)'''

'''a=eval(input())
n,m=map(int,input().split(','))
if n<=len(a):
    for x in range (n,m):
        b=a.pop(x)
    print(a)
else:
    print('error')'''

'''a=eval(input())
b=[]
for i in a:
    if i >=2:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            b.append(i)
print(b)'''

'''a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if b%c==0:
    print('%d'%(b/c))
else:
    print('%.2f'%(d)) '''

'''a=list(map(str,input().split()))
n,m=map(int,input().split())
a[n],a[m]=a[m],a[n]
print(a)'''

'''a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>0:
    for x in range(b):
        a.remove(max(a))
if len(a)>0:
    for x in range(c):
        a.remove(min(a))
print(a)'''

'''a=eval(input())
for x in reversed(a):
    if a.count(x)>1:
        for i in range(0,a.count(x)-1):
            a.remove(x)
print(a)'''

'''a=[]
n=eval(input())
for x in range(1,n+1):
    a.append(x)
b=a[0]
for i in range(n-1):
    a[i]=a[i+1]
a.insert(-1,b)
a.pop(-1)
print(a)'''

'''a = eval(input())
a.sort()
a.reverse()  # 使用 reverse 方法反转列表
s = ''.join(map(str, a))  # 将列表中的数字转换为字符串并拼接起来
s = int(s)  # 将结果字符串转换为整数
print(s)'''

'''a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
if len(b)>0:
    b.sort()
    b=','.join(map(str,b))
    print(b)
else:
    print("False")'''

a=eval(input())
b=[]
for x in a:
    if x==0:
        a.remove(x)
        b.append(x)
c=a+b
print(c)

