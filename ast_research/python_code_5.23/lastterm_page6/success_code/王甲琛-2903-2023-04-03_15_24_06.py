def main():
    num = eval(input())
    calculate_e(num)
def calculate_sum(a):
    list0=[]
    for i in range(a+1):
        b=str(a)*i
        list0.append(b)  
    list0.pop(0)
    list0=list(map(int,list0))
    print(sum(list0))
main()


