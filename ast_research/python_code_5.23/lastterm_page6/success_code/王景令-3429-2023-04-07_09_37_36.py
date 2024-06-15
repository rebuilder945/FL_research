a = input()
s1 =0
s2 = 0
s3 = 0
s4 = 0
for i in a:
    if i in 'abcdefghigklmnopqrstuvwxyz':
        s1 += 1
    elif i == ' ':
        s2 += 1
    elif i in '1234567890':
        s3 += 1
    else:
        s4 += 1
print(s1,s2,s3,s4,sep = ' ')
