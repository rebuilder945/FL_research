n=input()
g=eval(input())
while(n):
    pop_n=n.pop()
    if pop_n in n:
        continue
    else:
        g.insert(0,pop_n)
print(n)



