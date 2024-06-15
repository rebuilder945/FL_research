def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    l=[]
    for i in range(a):
        b=int(str(a)*(i+1))
        l.append(b)
    s=sum(l)
    print(s)
main()

