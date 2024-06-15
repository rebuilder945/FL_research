a=eval(input())
b,c=eval(input())
if b<0 and b>=len(a):
   print("error") 
else:

    del a[b:c]
print(a)
