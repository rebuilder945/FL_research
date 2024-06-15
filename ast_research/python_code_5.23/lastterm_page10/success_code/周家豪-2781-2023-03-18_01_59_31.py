id=input()
lstxishu="7-9-10-5-8-4-2-1-6-3-7-9-10-5-8-4-2".split("-")
sum=0
for i in range(len(id)-1):
    sum+=int(id[i])*int(lstxishu[i])
mod=sum%11
if len(id)!=18:
    print('Error')
elif id[17]==str((12-mod)%11) and not id[17].isupper():
    print('Correct')
elif id[17]=="X" and mod==2:
    print("Correct")
else:
    print('Wrong')

