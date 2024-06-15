nums = eval(input())
ls = []
for i in nums:
    if nums.count(i) == 1:
        ls.append(i)
ls.sort(reverse = False)        
if ls == []:
    print("False")
else:
    print(*ls,sep=",")            

        

         

           
           
