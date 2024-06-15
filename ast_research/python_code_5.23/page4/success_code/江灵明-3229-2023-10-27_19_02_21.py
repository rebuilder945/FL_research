a = list(eval(input()))
b = []
for i in a :
    if a.count(i)==1:
        b.append(i)
    b.sort(reverse=False)
    if b==[]:
        print(False)

