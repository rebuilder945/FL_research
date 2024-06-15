list = eval(input())
count = {}
for str in list:
    for char in str:
        if char not in count:
            count[char]=1
        else:
            count[char]+=1
            for i in sorted(count.keys()):
                print("%s,%d"%(i,count[i]))          




