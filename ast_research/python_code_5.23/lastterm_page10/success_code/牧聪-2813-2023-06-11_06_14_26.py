f=open(input(),"r")

for  line  in  f.readlines():
    line  =  line.strip('\n')
    print(line)

f.close()
