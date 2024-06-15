def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    x=1
    list=[]
    for i in range(num):
        e=e/x
        x+=1
        list.append(e)
    h=sum(list)+1
    print("%.6f"%(h))
main()


