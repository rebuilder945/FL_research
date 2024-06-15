a=eval(input())
b="".join(a)
c=",".join(b)
d=c.split(",")
for i in range (26):
    if d.count(chr(97+i))>0:
        print(chr(97+i),d.count(chr(97+i)),sep=",")












        



    








