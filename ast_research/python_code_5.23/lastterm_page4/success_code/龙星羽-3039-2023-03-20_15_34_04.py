lie=list(eval(input()))
d=max(lie)
x=min(lie)
for i in range(1,len(lie)):
    while d in lie:
        lie.remove(d)
    break
for i in range(1,len(lie)):
    while d in lie:
        lie.remove(x)
    break
print(lie)

