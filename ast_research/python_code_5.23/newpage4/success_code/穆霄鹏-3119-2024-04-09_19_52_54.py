ls=eval(input())
ls2=reversed(str(ls))
eval(ls2)
for x in ls2:
    if x not in ls2:
        ls2.append(x)
print(eval(reversed(str(ls2))))
