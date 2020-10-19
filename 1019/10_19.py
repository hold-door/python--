#元组,字符串

#元组
#和列表相似，但是不能改变
#列表[],元组（）

tuple1 = (1,'2','三','four')
print(tuple1)
print(tuple1[1])
thpe = type(tuple1[1])
print(thpe)
print(tuple1[2:])
print(tuple1)
tuple2 = tuple1[:]
print(tuple2)

#元组的标志是 ',' 不是 （）
temp = (1)
print(type(temp))#int
temp = (1,)
print(type(temp))#tuple
temp = 1,
print(type(temp))#tuple
temp = ()
print(type(temp))#tuple

print(8*(8,))#(8,8,8,8,8,8,8,8)     （，）是元组，'*'相当于复制运算，
print(8*[8])#[8,8,8,8,8,8,8,8]      []是列表，'*'相当于复制运算，与元组相似

#更新和删除元组
#切片的方式
#更新
tuple1 = (1,'2','三','four')
tuple1 = tuple1[:2] + ('2.5',) + tuple1[2:]#('2.5',)不要忘记','
print(tuple1)   #(1, '2', '2.5', '三', 'four')
#删除，切片切除
tuple1 = tuple1[:2] + tuple1[3:]    #(1, '2', '三', 'four')删除了2.5
print(tuple1)

#字符串
#与元组类似，都不能直接修改，但是可以通过切片方式修改
str1 = 'I love myself'
print(str1)
print(str1[:6])

#切片插入字符串
str2 = str1[:6] + '插入字符串' +str1[6:]
print(str1)
print(str2)






