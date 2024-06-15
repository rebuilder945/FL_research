yushu=[0,1,2,3,4,5,6,7,8,9,10]
weihao=[1,0,'X',9,8,7,6,5,4,3,2]
xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
jiaoyanma=0
id=input()
if len(id)!=18:
    print('Error')
else:
    for i in range(17):
        jiaoyanma+=int(id[i])*int(xishu[i])
    yu=jiaoyanma%11
    if weihao[yu]==int(id[-1]) or weihao[yu]==id[-1]:
        print('Correct')
    else:
        print('Wrong')

