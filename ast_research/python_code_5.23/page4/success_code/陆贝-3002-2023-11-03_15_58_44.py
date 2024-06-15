lt=eval(input())
a=len(lt)
b=sum(lt)
c=b/a
if c==int(c):
    print(int(c))
else:
    print("{:.2f}".format(c))
