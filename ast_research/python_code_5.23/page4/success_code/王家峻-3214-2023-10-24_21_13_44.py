n=eval(input())
# def yi(b):
#     t=[i for i,x in enumerate(b) if x==0]
#     l=[ i for i, x in enumerate(b) if x !=0]
#     if l == []:
#         return b
#     else:
#         for i in reversed(t):
            
#     return b
c=n.count(0)
for i in range(c):
        n.remove(0)
for x in range(c):
    n.append(0)
print(n)
    
# n=yi(n)


