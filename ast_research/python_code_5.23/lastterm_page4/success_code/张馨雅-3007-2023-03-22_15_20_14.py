Li=eval(input())
n,m=eval(input())
if m<=len(Li):
    for i in range(len(Li)):
        if i>=n and i<m:
            del Li[i]
else:
    print('error')
print(Li)






