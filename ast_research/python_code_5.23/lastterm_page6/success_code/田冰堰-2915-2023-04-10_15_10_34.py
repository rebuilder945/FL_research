a=eval(input())
if a<153:
    print("none")
else:
    for x in range(10):
        for y in range(10):
            for z in range(10):
                s1=100*x+10*y+z
                s2=x**3+y**3+z**3
                if s1==s2 and 100<s1<a:
                    print(s1)
                    
