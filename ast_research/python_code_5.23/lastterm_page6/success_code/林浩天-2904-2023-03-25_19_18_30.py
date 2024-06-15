def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(b):
        c=0
        d=[]
        s=str(b)
        for i in range(1,b+1):
                d.append(s*i)
                c+=int(s*i)
        print(f"{c} = {'+'.join(d)}")
main()

