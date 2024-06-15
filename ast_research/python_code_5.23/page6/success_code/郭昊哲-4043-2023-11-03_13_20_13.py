a=eval(input())
b="".join(a)
c=",".join(b)
d=c.split(",")
for i in range (26):
    if c.count(chr(97+i))>0:
        print(chr(97+i),c.count(i),sep=",")











        



    








