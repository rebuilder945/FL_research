def max_num(lt):
    m=len(lt)
    for i in range(m-1):
        for j in range(m-1-i):
            if str(lt(j))+str(lt[j+1])<str(lt[j+1])+str(lt[j]):
    t=""           
    for p in lt: 
        t+=str(p)
    return int(t)
lt=[0,1,2,3,2]
print(max_sort(lt))        
