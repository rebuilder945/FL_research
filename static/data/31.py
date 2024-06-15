a = 100
b = 100.123
c = "this is string"
# 错误写法：print("this is int type:%d,this is float type:%.3f, this is str type:%s"(a,b,c))
print("this is int type:%d,this is float type:%.3f, this is str type:%s"%(a,b,c))