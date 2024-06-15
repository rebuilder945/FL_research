def generate_arthmetic_sequence(n,m,l):
    result=[]
    for i in range(m):
        value=n+i*l
        result.append(value)
    return result
n,m,l=eval(input())
lst=generate_arthmetic_sequence(n,m,l)
print(lst)

