n=eval(input())
max_=max(n)
min_=min(n)
for x in range(n.count(max_)):
    n.remove(max_)
for y in range(n.count(min_)):
    n.remove(min_)
print(n)
