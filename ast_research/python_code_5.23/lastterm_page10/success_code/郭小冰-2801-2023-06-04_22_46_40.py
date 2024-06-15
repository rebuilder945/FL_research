P1_list=[]
P2_list=[]
P3_list=[]
P5_list=[]
p=input()
if len(p) >= 8:    
    d=1
else:    
    d=0
for x in p:    
    if x in "1234567890":        
        P1_list.append(x)    
    elif x in "abcdefghijklmnopqrstuvwxyz":        
        P2_list.append(x)    
    elif x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":        
        P3_list.append(x)    
    elif x in "~!@#$%^&*()_=-/,.?<>;{\:[}]|":        
        P5_list.append(x)
    if len(P1_list) != 0:    
        d += 1
        if len(P2_list) != 0:    
            d += 1
            if len(P3_list) != 0:    
                d += 1
                if len(P5_list) != 0:    
                    d += 1
    print(d)
