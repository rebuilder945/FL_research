Words=input().split(" ")
n,m=eval(input())
a=Words[n]
b=Words[m]
Words[n]=b
Words[m]=a
print(Words)
