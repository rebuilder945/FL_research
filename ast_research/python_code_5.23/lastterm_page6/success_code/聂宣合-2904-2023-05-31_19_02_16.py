def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    
    lst=[]
    sum=0
    for i in range(1,int(a)+1):
        mid=str(a)*i
        lst.append(int(mid))
    for i in lst:
        sum+=int(i)
    print(sum)
main()

