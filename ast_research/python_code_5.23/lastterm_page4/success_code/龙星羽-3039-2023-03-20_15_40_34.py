lie=eval(input())
d=max(lie)
x=min(lie)
while d in lie:
        lie.remove(d)
while x in lie:
        lie.remove(x)
print(lie)

