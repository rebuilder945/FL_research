def exchange(x):
	m=ord(x)
	if m in range(97,123):
		return chr(96*2+26-m+1)
	else:
		return chr(64*2+26-m+1)
a=input()
s=""
for x in a:
	if ord(x) in range(97,123):
		s+=exchange(x)
	else:
		s+=x
print(f"{a}\n")
print(s)

