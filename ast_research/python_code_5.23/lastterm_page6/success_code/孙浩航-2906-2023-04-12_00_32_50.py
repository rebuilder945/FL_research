def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        
        if total_count==1 or total_count==2:
            day=1
            return(print(day))
        else :
            day=0
            while total_count>=2:
                total_count=total_count/2-2
                day=day+1
                if 0<total_count<2:
                    day+=1
            return(print(day))
        
                      
main()


