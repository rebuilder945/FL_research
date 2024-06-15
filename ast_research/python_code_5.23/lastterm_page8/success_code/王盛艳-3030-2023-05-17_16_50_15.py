sName = input().split(',')
s1 = list(sName)
s2 = eval(input())
s3 = ()
s4 = []
for x in range(len(s1)):
    s3 = (s1[x],s2[x])
    s4.append(list(s3))
print(s4)
