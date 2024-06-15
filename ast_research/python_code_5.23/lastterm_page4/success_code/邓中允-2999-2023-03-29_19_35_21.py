a=input()
b,c=map(eval(input()))
temp=a[b]
a[b]=a[c]
a[c]=temp

print(a)
