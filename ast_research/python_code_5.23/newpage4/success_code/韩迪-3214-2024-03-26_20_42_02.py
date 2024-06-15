a=list(eval(input()))
b=a.count(0)
for i in range(b+1):
    if i>0:
        a.append(0)
        a.remove(0)
    else:
        pass
print(a)



# print(b)
