lst=input()
n=eval(input())
m=eval(input())
if n>=len(lst)-1 or n<0:
    print('error')
else:
    for x in range(m):
        lst.append(lst[n])
print(lst)
