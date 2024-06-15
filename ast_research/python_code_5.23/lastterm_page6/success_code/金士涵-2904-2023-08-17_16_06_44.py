def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=1
    b=0
    c=0
    lst=[]
    z=str(a)
    lst2=[]
    for x in z:
        lst2.append(x)
    d=len(lst2)
    while n<=a:
        b=b+a*(10**c)
        lst.append(b)
        n+=1
        c+=d
    v=sum(lst)
    print(v)
         
main()

