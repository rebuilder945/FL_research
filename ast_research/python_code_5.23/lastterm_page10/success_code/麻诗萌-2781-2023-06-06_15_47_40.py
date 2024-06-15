n=list(input())
if len(n)==18:
    s=0
    lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    dic2={'0':'1','1':'0','2':"X",'3':'9','4':'8','5':'7','6':'6','7':'5','8':'4','9':'3','10':'2'}
    for i in range(len(n)-1):
        n[i]=int(n[i])
        s=s+n[i]*lst1[i]   
    n=s%11
    if dic2[str(n)]==n[-1]:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Error")


    
