ls=eval(input())
ls2=reversed(str(ls))
for x in ls2:
    if x not in ls2:
        ls2.append(x)
print(reversed(str(ls2)))
