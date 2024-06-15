def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    for i in range(1,a+1):
        x=0
        for j in range(1,i+1):
            x+=a*(10**(j-1))
        sum+=x
    print(sum)        
main()

