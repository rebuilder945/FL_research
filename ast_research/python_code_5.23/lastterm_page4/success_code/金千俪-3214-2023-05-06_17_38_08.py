lst=eval(input())
for x in lst[:]:
    if x == 0:
        lst.insert(len(lst),x)
        lst.remove(x)
print(lst)

