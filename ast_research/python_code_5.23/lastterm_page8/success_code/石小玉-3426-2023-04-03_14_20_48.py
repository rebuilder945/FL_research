f=open("score.txt","r")
information=[]
for line in f.readlines():
    a=list(line.split(","))
    information.append([a[0],a[1],int(a[2]),int(a[3]),int(a[4])])  
    #这一步非常关键，不能不加int，否则无法去除换行符，从而导致后续出错
information.sort(key=lambda x:-(x[2]+x[3]+x[4]))
f.close()

f=open("sorted.txt","w")
for x in information:
    f.write("{},{},{},{},{}".format(x[1],x[0],x[2],x[3],x[4]))
    f.write("\n")
    #这一步相当于人工手动换行，也可以使用end函数
f.close()


