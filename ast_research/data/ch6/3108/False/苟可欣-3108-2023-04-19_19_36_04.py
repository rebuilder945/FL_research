from traceback import print_tb


str=eval(input())
for st in str:
    for i in st:    
        k=0
        for s in str:                
            for i1 in s:
                if i1==i:
                    k=k+1
        print("%.s,%.d"%(i,k))

