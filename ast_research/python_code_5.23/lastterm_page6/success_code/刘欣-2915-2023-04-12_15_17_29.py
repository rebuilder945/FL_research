zhengshu=str(input())
he=0
for i in zhengshu:
    i=int(i)
    he += i**3
if he==zhengshu:
    print(he)
else:
    print("none")
