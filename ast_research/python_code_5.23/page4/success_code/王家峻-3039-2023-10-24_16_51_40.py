n=eval(input())
for x in n:
    if x ==max(n):
        n.remove(x)
for i in n:
   if i ==min(n):
       n.remove(i)
print(n)
