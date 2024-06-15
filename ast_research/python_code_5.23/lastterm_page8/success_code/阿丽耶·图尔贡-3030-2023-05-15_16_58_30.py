f = open('data.txt', 'w+')
f.write("sno\tsname\tsage\n")
ls = []
stext = input() or "End"
while stext != "End":    
    ls.append(stext)    
    stext = input() or "End"
ls.sort()
for line in ls:    
    stu = line.split(",")    
    f.write("{}\t{}\t{}\n".format(stu[0], stu[1], stu[2]))
f.seek(0)
print(f.read())


