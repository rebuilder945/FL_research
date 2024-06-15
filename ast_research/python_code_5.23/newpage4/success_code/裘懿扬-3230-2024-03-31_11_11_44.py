a=list(eval(input()))
a.sort(reverse=True)
b=''.join(str(z) for z in a)
print(int(b))

