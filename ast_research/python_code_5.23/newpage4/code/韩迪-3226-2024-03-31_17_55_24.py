def search(a)
       a=list(eval(input()))
       s=[]
       for i in a:
             if a.count(i)>n//2:
                    s.append(i)
             else:
                    pass
       if bool(s)=False:
             return("False")
       else:
             return(s)





nums = eval(input())
y = search(nums)
print(y)


