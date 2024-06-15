abc=str(input())
ls=[int(x) for x in abc]
for i in range(3):
    ls[i]=(ls[i]+5)%10
m=ls[0]
del ls[0]
ls.insert(0,ls.pop())
ls.append(m)
result="".join(map(str,ls))
print(result)



