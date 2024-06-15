a=eval(input())
b=sorted(a,reverse=True)
string="".join(map(str,b))
for x in string:
    if x==0:
        print("0")
    else:
        print(string)
