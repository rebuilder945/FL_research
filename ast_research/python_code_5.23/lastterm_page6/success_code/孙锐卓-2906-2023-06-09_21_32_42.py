def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    n=1
    if x%2==0:
        x=x-x/2
        if x-2<=0:   
            print(n)
        else:
            x=x/2-2
            n+=1
    else:
        x=x-(x-1)/2
        if x-2<=0:
            print(n)
        else:
            x=x-2
        
    
        

main()


