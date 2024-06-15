from cgi import print_arguments


a=eval(input())
b=[]
for i in range(len(a)-1,-1,-1):
    if a[i] not in b:
        b.append(a[i])
b=b.sort(reverse=True)
print(b)
