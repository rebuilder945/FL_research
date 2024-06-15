a=eval(input())
for i in a:
    dick=a.count(i)
    for x in range(int(dick)-1):
        a.remove(i)
print(a)
