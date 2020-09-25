'''
print("-------------改进游戏-----------")
temp = input("猜猜阿多喜欢哪个数字")
luck = 4
if(temp == luck):
    print("SUCCESS!!")
else:
    print("lucky number = 4")
print('Game over!')
'''
print("-----------------猜数字游戏-------------")
guess = input("猜猜我喜欢几号")
#ans = 4
if(guess > 4):
    print("猜错啦，再小点")
if(guess < 4):
    print("猜错啦，再大点")
else:
    print("GOD BOY!")
print("Congualations!")
