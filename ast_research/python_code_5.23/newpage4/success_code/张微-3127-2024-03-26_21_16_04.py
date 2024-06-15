num=eval(input())
t=0
text=[x for x in range(1,num+1)]
# print(text)
for i in range(1,len(text)):
    t=text[i]
    text[i]=text[i-1]
    text[i-1]=t
print(text)

