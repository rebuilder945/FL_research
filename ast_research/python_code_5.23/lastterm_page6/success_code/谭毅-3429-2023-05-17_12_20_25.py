dummy= list(input())
ENG=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUM=["1","2","3","4","5","6","7","8","9",'0']
i=0
j=0
k=0
p=0
for x in dummy:
    if x in ENG:
        i = i+1
    elif x in NUM:
        j= j+1
    elif x == " ":
        k = k+1
    else:
        p=p+1
print(i,k,j,p,end="")

