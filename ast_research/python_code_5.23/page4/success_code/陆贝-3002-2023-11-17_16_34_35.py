lt=eval(input())
a=len(lt)
b=sum(lt)
c=b/a
t=int(c)
if c==t:
    print(t)
else:
    print("{:.2f}".format(c))
