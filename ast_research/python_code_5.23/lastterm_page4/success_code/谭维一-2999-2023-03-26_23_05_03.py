str = input().split(" ")
n,m = map(int,input().split(" "))
x = str[n]
str[n] = str[m]
str[m] = x
print(str)
