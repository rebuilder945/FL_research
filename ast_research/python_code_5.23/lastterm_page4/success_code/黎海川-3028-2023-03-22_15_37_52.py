v1=[x for x in range(-5,+10,2)]
v2="".join([chr(ord('a')+x)for x in range(26)  ])
print("v1:",v1)
print("v2:",v2)
print(v1[0:5])
print(v1[-6:7])
print(v1[-1:10])
print(v2[0:26])
print(v2[::-5])
print(v2[::-1])



