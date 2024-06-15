n=eval(input())
ping=sum(n)/len(n)
if ping==int(ping):
    print(int(ping))
else:
    print("{:.2f}".format(ping))
