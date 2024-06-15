def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    lst=[]
    for x in range(a):
        lst.append(str(int(a))*(x+1))
    ls2=[int(x) for x in lst]   
    s=sum(ls2)
    print(s)  
main()

