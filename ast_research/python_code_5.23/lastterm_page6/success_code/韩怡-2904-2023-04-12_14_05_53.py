def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    sum=0
    for i in range(1,x+1):
        b=int(str(x)*i)
        sum += b
    print(sum)
main()

