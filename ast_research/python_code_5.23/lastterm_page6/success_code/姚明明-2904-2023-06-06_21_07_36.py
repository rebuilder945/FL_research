def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    for i in range(1,a+1):
        d=[]
        b=int(str(a)*i)
        d.append(b)
        s=sum(d)
    return s
    
main()

