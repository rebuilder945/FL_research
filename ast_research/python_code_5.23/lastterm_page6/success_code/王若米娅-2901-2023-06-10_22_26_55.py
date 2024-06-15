n=input()or'#'
s=0
c=0
while n!="#":
    s+=eval(n)
    c+=1
    n=input()or"#"
print(c,s)
