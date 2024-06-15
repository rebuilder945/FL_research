def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
    list0=[b]
    x=len(str(b))
    d=b
    for i in range(x,b,x):
        b=d*(10**i)+b
        list0.append(b)
    total=sum(list0)
    print(total)
main()

