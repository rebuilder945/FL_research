n=eval(input())
b=sum(n)/len(n)
if b==int(b):
    print('%.0f',(b))
else:
    print("%.2f",(b))
