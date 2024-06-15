n=eval(input())
def keep(n):
    seen=set()
    result=[]
    for i in reversed(n):
        if i in seen:
            result.append(i)
        else:
            seen.add(i)
    return result[::-1]
b=keep(n)
# b=[]
# for i in n
# [b.append(i) for i in n if not i in b]
# b=list(set(n))
print(b)
