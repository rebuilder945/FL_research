def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst1=[1]
    jishu=1
    for i in range(1,num+1):
            jishu=jishu*i
            lst1.append(1/(jishu))
    print("%.6f"%(sum(lst1)))
main()


