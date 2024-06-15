n=eval(input())
c=n[::-1]
def keep(c):
    result=[]
    for i in c:
        if i not in result:
            result.append(i)
    return result
b=keep(c) 
t=b[::-1]
# [b.append(i) for i in n if not i in b]
# b=list(set(n))
print(t)
