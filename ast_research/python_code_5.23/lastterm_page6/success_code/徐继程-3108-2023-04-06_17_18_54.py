lst=eval(input())
end="0"
for x in range(len(lst)):
    end+=lst[x]
for i in range(ord('a'),ord('z')+1):
    ii=chr(i)
    num=end.count(ii)
    if num>0:
        print('%s %d'%(ii,num))


