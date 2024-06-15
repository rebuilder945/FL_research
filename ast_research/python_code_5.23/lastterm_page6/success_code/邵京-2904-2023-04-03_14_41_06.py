def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
    list0=[b]
    d=b
    for i in range(1,b):
        b=d*(10**i)+b
        list0.append(b)
    total=sum(list0)
    print(sum)
main()

