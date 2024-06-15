s=input()
words=s.split()
count=len(words)
length=sum(len(word) for word in words)
a=length/count
print(count,end=','"%.2f"%a)
