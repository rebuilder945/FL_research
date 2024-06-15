a=eval(input())
b="".join(a)
for x in range(97,123):
    s=b.count(chr(x))
    if s>0:
        print(chr(x),s,sep=",")


