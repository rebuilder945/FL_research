def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        i=0
        if total_count%2!=0: 
           a=math.floor(total_count/2)
           total_count=total_count-a-2
           i+=1
           if  total_count<=0:
               break
           else:
                   countinue
        else:
               a=total_count/2
               total_count=total_count-a-2
               i+=1
               if  total_count<=0:
                   break
               else:
                       countinue
        print(i）  
              
                      
            
                  
main()


