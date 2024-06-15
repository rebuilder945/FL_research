def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        s=str(a)
        q=[]
        for i in range(1,a+1):
                t=a*i
                z=eval(t)
                q.append(z)
        p=sum(q)
        print(p)
main()

