l=input().split()
m=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',\
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',\
     't', 'u', 'v', 'w', 'x', 'y', 'z',\
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',\
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=["1","2","3","4","5","6","7","8","9",'0']
a,b,c,d=0,0,0,0
for x in l:
    if x in m:
        a+=1
    elif x in n:
        b+=1
    elif x == " ":
        c+=1
    else:
        d+=1
print(a,b,c,d,end=" ")

