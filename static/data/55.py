lst = eval(input())
print("%.2f" % (sum(lst) / len(lst)))
#len() 函数不能直接应用于类型对象（type），因为它期望一个序列或集合类型，而不是一个类型对象。