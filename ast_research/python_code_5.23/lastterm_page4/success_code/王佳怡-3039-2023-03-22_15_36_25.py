l=list(eval(input()))
a=max(l)
b=min(l)
for i in len(l):
    if l[i]==a or l[i]==b:
        del l[i]
print(l)
