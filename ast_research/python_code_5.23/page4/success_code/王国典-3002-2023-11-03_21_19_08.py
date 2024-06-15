Is=eval(input())
ping=sum(Is)/len(Is)
if ping-int(ping)==0:
    print(int(ping))
else:
    print("%.2f"%(ping))

