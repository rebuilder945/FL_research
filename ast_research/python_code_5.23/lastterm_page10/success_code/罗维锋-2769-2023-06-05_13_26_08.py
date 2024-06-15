def exchange(x):
	m=ord(x)
	return chr(26-m+97+1)
a=input()
s=""
for x in a:
	if ord(x) in range(97,123):
		s+=exchange(x)
	else:
		s+=x
print(f"{a}\n")
print(s)

