# member = ['嘿嘿黑黑','白白','纷纷粉','绿绿','花花','红红洪洪红']
# print(member)
# number = [1,2,3,4,5]
# print(number)
# mix = [1,'da','激素',[1,2,3]]
# print(mix)
# empty = []
# print(empty)

# number.append('da')
# print(number)
# print(len(number))
# number.extend(['xiao','fei'])
# print(number)
# number.insert(0,'牡丹')
# print(number)
# print(number[1])
# temp = number[0]
# number[0] = number[1]
# number[1] = temp
# print(number)
# number.remove(2)
# print(number)
# del number[1]
# print(number)

# number = [1,2,'3','four','五']
# print(number)
# print(number.pop())
# print(number)
# number.remove('3')
# print(number)
# del number[1]
# print(number)

# number = [1,2,'3','four','五']
# print(number)
# print(number[1:3])#原列表没有变，分片只是拷贝
# print(number)#原列表没有变

list1 = [132,156]
list2 = [133]
print(list1<list2)
list3 = [134,245]
print(list1 < list2 and list1 < list3)
list4 = list1 + list2
print(list4)
list1.extend([167])
list1 *= 3
print(list1)
print(132 in list1)
