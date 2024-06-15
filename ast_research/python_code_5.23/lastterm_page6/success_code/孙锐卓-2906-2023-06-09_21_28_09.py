def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    n=1
    if x%2==0:
        x=x/2
        if x/2-2<=0:   
            print(n)
        else:
            n+=1
    
        

main()


