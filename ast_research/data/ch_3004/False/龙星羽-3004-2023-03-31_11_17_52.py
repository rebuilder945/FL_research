v1=[x for x in range(-5,+10,2)]
v2="".join([chr(ord('a')+x) for x in range(26)])
print("v1:",v1)
print("v2:",v2)
print(v1[0:5])
print(v1[-6:-1])
print(v1[-1:-7:-2])
print(v2[:])
print(v2[::-5])
print(v2[::-1])
print(v2[:-5:7])

