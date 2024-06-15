def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        i=0
        while total_count  >0:
                 if total_count%2==0:
                    total_count=total_count/2-2
                    i+=1
                 else:
                    total_count= (total_count-3)/2
                    i+=1
        print(i)                  
                       
              
                      
            
                  
main()


