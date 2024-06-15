num=''
lst=[]
while True:
    num=input()
    lst.append(num)
    if num=='#':
        break
lst.remove('#')
n=len(lst)
lst=map(int,lst)
s=sum(lst)
print(n,s)

