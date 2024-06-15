dic_code={}
for i in range(26):
    orgin=chr(ord("a")+i)
    after=chr(ord("a")+25-i)
    dic_code[orgin]=after
for j in range(26):
    orgin1=chr(ord("A")+j)
    after1=chr(ord("A")+25-j)
    dic_code[orgin1]=after1

code=input()
print(code)
for k in code:
    if k.isalpha():
        print(dic_code[k],end="")
    else:
        print(k,end="")




