text_in=open("score.txt","r")
text=text_in.read().split()
di_nums=[]
for x in text:
    di_nums.append(x.split(","))
for x in di_nums:
    a=x[0]      
    b=x[1]
    x.remove(a)
    x.remove(b)
    x.insert(0,a)   
    x.insert(0,b)      
di_nums.sort(key=lambda x:(int(x[2])+int(x[3])+int(x[4])), reverse=True)
text_out=open("sorted.txt","w")
for x in di_nums:
    text_out.write(x[0]+","+x[1]+","+x[2]+","+x[3]+","+x[4])
    text_out.write("\n")

