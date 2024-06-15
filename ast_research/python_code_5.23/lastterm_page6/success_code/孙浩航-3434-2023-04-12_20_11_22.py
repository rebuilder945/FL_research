a=input()
b=input()
sl={a,b}
s2={'red','blue'}
s3={'red','yellow'}
s4={'blue','yellow'}
s5={'blue','yellow','red'}
if a not in s5 or b not in s5 or a==b:
    print("error")
elif sl==s2:
    print("purple")
elif sl==s3:
    print("orange")
else:
    print("green")
