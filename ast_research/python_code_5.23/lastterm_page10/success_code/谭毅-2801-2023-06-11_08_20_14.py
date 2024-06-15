a=input()
ls=[]
q,s,d,f,g=0,0,0,0,0
for x in a:
    if x.isalpha() :
        if x.upper()==x and q==0:
            if x.lower!=x:
                q+=1
            else:
                pass
        else:
            if g==0:
                g+=1

    elif x in ['0','1','2','3','4','5','6','7','8','9'] and s==0:
         s+=1
    elif len(a)>=8 and d==0:
         d+=1
    elif x in ['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\'] and f==0:
        f+=1
    else:
         pass
print(q+s+d+f+g)
