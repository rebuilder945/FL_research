a = eval(input())
sum =0
fenmu=1
fenzi=2

for i in range(a):
    
    sum= sum+fenzi/fenmu
    fenzi,fenmu=fenmu+fenzi,fenzi
    
    

    
    print("%.4f"%(sum))
    

