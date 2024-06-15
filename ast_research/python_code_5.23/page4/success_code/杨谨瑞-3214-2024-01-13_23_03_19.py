str1 = input()
li1 = list(map(int, str1[1:-1].split(',')))
for i in range(len(li1)):
    if li1[i]==0:
        del li1[i]
        li1=li1+[0]
print(li1)

