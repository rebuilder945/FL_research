a= list(eval(input()))
a.sort(reverse=True)
b=''.join(str(i) for i in a)

print(b)
