def exchange(x):
	m=ord(x)
	if m in range(97,123):
		return chr(96*2+26-m+1)
	else:
		return chr(96*2+26-m+1).upper()
a=input()
s=""
for x in a:
	if ord(x) in range(97,123) or range(65,91):
		s+=exchange(x)
	else:
		s+=x
print(a)
print(s)

