n=eval(input())
m=eval(input())
if int(m[1])>len(n):
    print("error")
else:
    if int(m[0])>int(m[1]):
        print("error")
    else:
        del n[int(m[0]):int(m[1])]
        print(n)
