def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    num=[]
    for x in range(1,a+1):
        s=[str(a) for i in range(x)]
        num.append("".join(s))
    num2=[int(num[i])for i in range (len(num))]
    print(sum(num2))
main()

