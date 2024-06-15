count=0
a=0
lst=""
while True:
    lst=eval(input())
    if lst=='#':
        break
    a+=int(lst)
    count+=1
print(count,a)



