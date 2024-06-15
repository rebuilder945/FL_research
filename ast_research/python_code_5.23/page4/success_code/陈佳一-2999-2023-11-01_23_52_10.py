a=input()
e=input()
c,d=eval(e.split(" "))
b=a.split(" ")
b[c],b[d]=b[d],b[c]
print(b)
