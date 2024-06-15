num=input()
for i in range(num):
    num[i]+=5
    num[i]=num[i]%10
#input() 函数返回的是字符串类型，而不是整数类型。
#因此，在使用 range() 函数时，它期望一个整数作为参数，而你给出的是一个字符串，导致了错误。
s=num[::-1]
print(s)

