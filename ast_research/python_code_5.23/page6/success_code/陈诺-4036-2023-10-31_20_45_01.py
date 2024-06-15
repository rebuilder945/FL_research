s={"jishu":"red","oushu":"black"}
m={'jishu':"black","oushu":"red"}
n=int(input())
if n==0:
    print("green")
elif(n>=1 and n<=10) or (n>=29 and n<=36):
    if n%2==0:
        print(m["oushu"])
    else:
        print(m["jishu"])
else:
    print("error")
