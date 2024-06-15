a=input()
b=eval(input())
a=a.split(',')
c=[[a[i],b[i]] for i in range(len(b))]
print(c)
