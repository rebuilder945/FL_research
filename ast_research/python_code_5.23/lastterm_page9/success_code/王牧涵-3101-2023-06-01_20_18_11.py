class Book:
        def __init__(self, name, number, price):
            self.name = name # 书名
            self.number = number # 书号
            self.price = price # 单价

    # 析构函数
        def __del__(self):
            print(f"Book destroyed-{self.name},{self.number},{round(self.price, 2)}") # 打印对象被销毁时的信息，单价保留两位小数


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

