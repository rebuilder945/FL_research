lst = eval(input())
mx = max(lst)
mn = min(lst)
new = []
for x in lst:
    if x != mx and x != mn:
        new.append(x)
print(new)

