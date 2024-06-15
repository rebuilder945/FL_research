def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    t=a
    sum = 0
    for i in range(a):
        sum += t
        t= t*10**i + a
       
    print(sum)

main()

