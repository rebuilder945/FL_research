def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        sum=0
        for i in range(1,a+1):        
            s=int("".join([str(a)*i]))
            sum+=s
        print(sum)
main()

