n=eval(input())
b=sum(n)/len(n)
if b==int(b):
    print(f"{b:.0f}")
else:
    print(f"{b:.2f}")
