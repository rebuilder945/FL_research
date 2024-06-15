s={"jishu":"red","oushu":"black"}
m={"jishu":"black","oushu":"red"}
n=int(input())
if n ==0:
    print("green")
elif (n<=10 and n>0) or (n<=28 and n>=19):
    if n%2==0:
        print(s["oushu"])
    else:
        print(s["jishu"])
elif (n>=11 and n<=18) or (n>=29 and n<=36):
    if n%2==0:
        print(s["oushu"])
    else:
        print(s["jishu"])
else:
    print('error')
