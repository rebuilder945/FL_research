lt=eval(input())
a=len(lt)
b=sum(lt)
c=b/a
if type(c)==int:
    print(c)
else:
    print("{:.2f}".format(c))
