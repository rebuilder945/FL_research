def work(a) :
    def jiecheng(i):
            if i<2:
                return 1
            else:
                return i*jiecheng(i-1)
    s=[]
    for mm in range(a+1):
        
        sm=(mm,jiecheng(mm))
        s.append(sm)
    return dict(s)
	

a = int(input())
ans = work(a)
print(ans)

