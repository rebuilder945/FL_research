def exchange(x):
	m=ord(x)
	return chr(26-m+1)
a=input()
s=""
for x in a:
	s+=exchange(x)
print(f"{a}\n")
print(s)

