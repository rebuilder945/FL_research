def liebiao(n):
    c = n+1
    a = [x for x in range(1,c)]
    return a 
n = eval(input())
b=liebiao(n)
m = b[0]
q = []
for x in range(len(b)-1):
    q.append(b[x+1])
q.append(m)
print(q)







