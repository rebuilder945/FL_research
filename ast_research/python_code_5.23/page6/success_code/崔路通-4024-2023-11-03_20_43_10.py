def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    lst=[]
    a=str(a)
    lst.append(a*(i+1) for i in range(int(a)))
    b=0
    for x in lst:
        b=b+int(x)
    print(b)
        
main()

