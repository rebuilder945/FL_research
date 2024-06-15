str1=input()
count_str={}
while (str1 !="q"):
    count_str.get(str1,0)+1
a=0
for i in count_str:
    if count_str[i]>a:
        a=count_str[i]
        c=i

print(c,a)


