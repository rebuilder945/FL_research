n=eval(input())
def keep(n):
    result=[]
    for i in n:
        if i not in result:
            result.append(i)
    return result
b=keep(n) 
# [b.append(i) for i in n if not i in b]
# b=list(set(n))
print(b)
