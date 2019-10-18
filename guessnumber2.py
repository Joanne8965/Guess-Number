# 讓使用者決定數值範圍去猜
# 猜對的話 印出 “ˊ終於猜對了！“
# 猜錯的話 要告訴他 比答案大/小
# V2 - 讓使用者決定數字範圍

import random
start = input('請決定隨機數字範圍開始值 Please insert a number begins with: ')
end = input('請決定隨機數字範圍結束值 Please insert a number ends with: ')
start = int(start)
end = int(end)


r = random.randint(start, end)  #隨機整數, r = 答案
count = 0

while True:                 #無限巡迴
    count += 1              #count = count + 1
    num = input('請猜數字 Guess a number: ')
    num = int(num)
    if num == r:
        print('你猜中了！You are right!')
        print('這是你猜的第', count, '次','You have tried', count, 'times')
        break
    elif num > r:
        print('比答案大 Too big!')
    elif num < r:
        print('比答案小 Too small!')
    print('這是你猜的第', count, '次','You have tried', count, 'times')

