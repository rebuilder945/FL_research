a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(q) for q in a.split(",")]
n=set(b)
print(n)
