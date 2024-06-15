def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    #b=int(a)
    for i in range(a):
        sum+=a
        a=str(a)
        aa=a+str(a)
        a=int(aa)
        
    print(sum)
main()

