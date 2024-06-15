def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    l=[]
    for i in range(1,a+1):
        b=int(str(a)*i)
        l.append(b)
        calculate_sum(a)=sum(l)
    print(calculate_sum(a))
main()

