a = eval(input())
for i in a:
    while i == max(a):
        a.remove(i)
for i in a:
    while i == min(a):
        a.remove(i)
print(a)
