a = input().strip("[]").split(",")
a.remove(max(a))
a.remove(min(a))
print(a)
