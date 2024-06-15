def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        x=[]
        for i in range(a):
                if i ==0:
                        c=a
                        x.insert(0,c)
                else:
                        c=a*10**i+x[0]
                        x.insert(0,c)
        s=sum(x)
        print(s)
main()
main()

