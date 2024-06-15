
s={1:"spring",2:"summer",3:"autumn",4:"winter"}
n=int(input())
if(n>=3 and n<=5):
    print(s[1])
elif(n>=6 and n<=8):
    print(s[2])
elif(n>=9 and n<=11):
    print(s[3])
elif(n==12 or n==1 or n==2):
    print(s[4])
else:
    print("error")






