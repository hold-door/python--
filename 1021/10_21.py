#字符串

str1 = 'gaotianyu'
str1 = str1.capitalize()#capitalize()   把首字母大写
print(str1)
str1 = str1.casefold()#casefold()   把整个字符串改成小写
print(str1)
str1 = str1.center(16)#center(width)  将字符串居中
print(str1)
str1 = str1.count('g',4,8)#count(sub[,start[,end]])   返回sub在字符串里出现的次数，start和end参数表示范围，可选
print(str1)
str1 = 'gaotianyu'
print(str1.endswith('yu'))#endswith(sub[,start[,end]]) 判断字符串是否以sub子字符串结束，如果是返回True，否则返回Flase
str2 = 'I\tlove\teating'
print(str2.expandtabs(1))#expandtabs([tabsize = 8])
print(str1.find('t'))#find(sub[,start[,end]])   如果存在返回字符串所在位置，如果不存在返回-1
print(str1.index('t'))#index和find一样，不过如果不存在，返回异常
