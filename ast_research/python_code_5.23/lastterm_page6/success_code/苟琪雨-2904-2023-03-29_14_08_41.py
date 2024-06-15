def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=str(a)
    lst=[]
    for i in range(1,a+1):
        c=b*i
        lst.append(c)
    for x in range(0,len(lst)):
        result=0
        result=result+int(lst[x])
    print(result)

main()

