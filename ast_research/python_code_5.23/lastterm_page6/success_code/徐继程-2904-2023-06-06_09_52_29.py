def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=a
    b=a
    a=str(a) 
   
    for i in range(b-1):
        aa=a+str(b)
        a=int(aa)
        sum+=a
        a=str(a)
    print(sum)

main()

