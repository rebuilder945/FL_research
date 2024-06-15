s = {1:"spring",2:"summer",3:"autumn",4:"winter"}
n = int(input())
if (3 <= n <= 5):
    print(s[1])
elif (6 <= n <= 8):
    print(s[2])
elif (9 <= n <= 11):
    print(s[3])
elif (n == 12 or n == 1 or n == 2):
    print(s[4])
else:
    print("error")                
