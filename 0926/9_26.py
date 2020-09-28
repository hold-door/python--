import random
'''
guess = input("猜猜阿多喜欢哪个数字：")
guess = int(guess)
num = 0
rand = random.randint(1,10)
while guess != rand:
    if(guess > rand):
        num += 1
        if(num == 3):
            print("Sorry!Game Over!")
            break
        else:
            print("猜错啦！再小点。")
            guess = input("猜猜阿多喜欢哪个数字：")
            guess = int(guess)
    else:
        num += 1
        if(num == 3):
            print("Sorry!Game Over!")
            break
        else:
            print("猜错啦！再大点。")
            guess = input("猜猜阿多喜欢哪个数字：")
            guess = int(guess)
if(guess == rand):
    print("恭喜你答对了！")
'''

logic = (3>2) and (1>2)
print(logic)
logic2 = (3>2) or (1>2)
print(logic2)