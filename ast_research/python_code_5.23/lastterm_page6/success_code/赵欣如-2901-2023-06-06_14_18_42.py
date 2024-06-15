n=input()or"#"
a=0
b=0
while n!="#":
    a+=1
    b+=int(n)
    n=input()or"#"
print(a,b)
