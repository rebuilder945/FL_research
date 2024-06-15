def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        x=[]
        for i in range(a):
                b=int(str(a)*(i+1))
                x.append(b)
        s=sum(x)
        print(s)

main()

