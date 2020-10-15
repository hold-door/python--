# number = [1,'2',"3",'four','五']
# print(number)
# print(number[1:3])
# print(number)
# print(number[:3])
# print(number[3:])
# print(number[:])
# number2 = number
# print(number2)

number = [1,'2',"3",'four','五',[6,'7']]
print(number)
print(6 in number)#false
print(dir(list))
print(number.count(123))

Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = [1,'2',"3",'four','五']
>>> number
[1, '2', '3', 'four', '五']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> number.count(1)
1
>>> number,index('2')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    number,index('2')
NameError: name 'index' is not defined
>>> number.index('2')
1
>>> number*3
[1, '2', '3', 'four', '五', 1, '2', '3', 'four', '五', 1, '2', '3', 'four', '五']
>>> number
[1, '2', '3', 'four', '五']
>>> number *= number
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    number *= number
TypeError: can't multiply sequence by non-int of type 'list'
>>> number *= 3
>>> number
[1, '2', '3', 'four', '五', 1, '2', '3', 'four', '五', 1, '2', '3', 'four', '五']
>>> number.index('2')
1
>>> number.index(1)
0
>>> number.index('four'3,9)
SyntaxError: invalid syntax
>>> number.index('four,3,9')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    number.index('four,3,9')
ValueError: 'four,3,9' is not in list
>>> number.index('four',3,9)
3
>>> number.reverse()
>>> number
['五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1]
>>> ['五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1]
['五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1]
>>> number
['五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1, '五', 'four', '3', '2', 1]
>>> number.sort()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    number.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> number = [1,2,3,4,5,6]
>>> number.sort()
>>> number
[1, 2, 3, 4, 5, 6]
>>> number = [4,5,7,3,5,2,3]
>>> number
[4, 5, 7, 3, 5, 2, 3]
>>> number.sort()
>>> number
[2, 3, 3, 4, 5, 5, 7]
>>> number.reverse
<built-in method reverse of list object at 0x0000000002C757C0>
>>> number
[2, 3, 3, 4, 5, 5, 7]
>>> number.reverse()
>>> number
[7, 5, 5, 4, 3, 3, 2]
>>> number.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    number.sort(reverse=true)
NameError: name 'true' is not defined
>>> number.sort(reverse=True)
>>> number
[7, 5, 5, 4, 3, 3, 2]
>>>
