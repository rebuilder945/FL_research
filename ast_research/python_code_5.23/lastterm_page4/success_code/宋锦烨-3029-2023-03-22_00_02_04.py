s1 = input().split(',')
s2 = eval(input())
s3 = list(s1)
s4 = ()
s5 = []
for i in range(len(s3)):
    s4=(s3[i],s2[i])
    s5.append(list(s4))
print(s5)




