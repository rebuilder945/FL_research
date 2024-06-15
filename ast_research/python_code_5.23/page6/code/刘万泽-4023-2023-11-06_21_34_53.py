def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        for i in range(100):
              if  total_count%2!=0: 
                 a=(N-1)/2
                 total_count=total_count-a-2
           
                 if  total_count<=0:
                       break
                 else:
                        countinue
              else:
                    a=total_count/2
                    total_count=total_count-a-2
              
                    if  total_count<=0:
                         break
                    else:
                          countinue
         print(i+1）  
              
                      
            
                  
main()


