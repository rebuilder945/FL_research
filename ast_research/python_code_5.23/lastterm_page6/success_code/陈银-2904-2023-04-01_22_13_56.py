def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(i):
    sum = 0
    for x in range(1,i+1):
        num = int(str(i)*x)
        sum += num
    print(sum) 
main()

