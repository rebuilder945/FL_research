sMessage = ""
sub =  []
while sMessage!= "#":
    sMessage = input()
    sub.append(sMessage)  
sun = [] 
for x in sub[0:len(sub)-1]:
    n = int(x)
    sun.append(n)
a = len(sun)
b = sum(sun) 
print(a,b)
    



