lst=eval(input())
#print(lst)
# 
m=27
n=2
l=0
abc=[]
while l<m:
    r=0
    line=[]
    while r<n:
        line.append(0)
        r+=1
    abc.append(line)
    l+=1
#print(abc)

abc[0][0]='a'
abc[1][0]='b'
abc[2][0]='c'
abc[3][0]='d'
abc[4][0]='e'
abc[5][0]='f'
abc[6][0]='g'
abc[7][0]='h'
abc[8][0]='i'
abc[9][0]='j'
abc[10][0]='k'
abc[11][0]='l'
abc[12][0]='m'
abc[13][0]='n'
abc[14][0]='o'
abc[15][0]='r'
abc[18][0]='s'
abc[19][0]='t'
abc[20][0]='u'
abc[21][0]='v'
abc[22][0]='w'
abc[23][0]='x'
abc[24][0]='y'
abc[25][0]='z'

for i in range(len(lst)):
    for j in lst[i]:
        if j=='a' : abc[0][1]+=1
        elif j=='b' : abc[1][1]+=1
        elif j=='c' : abc[2][1]+=1
        elif j=='d' : abc[3][1]+=1
        elif j=='e' : abc[4][1]+=1
        elif j=='f' : abc[5][1]+=1
        elif j=='g' : abc[6][1]+=1
        elif j=='h' : abc[7][1]+=1
        elif j=='i' : abc[8][1]+=1
        elif j=='j' : abc[9][1]+=1
        elif j=='k' : abc[10][1]+=1
        elif j=='l' : abc[11][1]+=1
        elif j=='m' : abc[12][1]+=1
        elif j=='n' : abc[13][1]+=1
        elif j=='o' : abc[14][1]+=1
        elif j=='p' : abc[15][1]+=1
        elif j=='q' : abc[16][1]+=1
        elif j=='r' : abc[17][1]+=1
        elif j=='s' : abc[18][1]+=1
        elif j=='t' : abc[19][1]+=1
        elif j=='u' : abc[20][1]+=1
        elif j=='v' : abc[21][1]+=1
        elif j=='w' : abc[22][1]+=1
        elif j=='x' : abc[23][1]+=1
        elif j=='y' : abc[24][1]+=1
        elif j=='z' : abc[25][1]+=1
#print(abc)

for i in range(26):
    if abc[i][1]!=0 : print(abc[i][0],abc[i][1],sep=',')
    
