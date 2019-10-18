# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 “ˊ終於猜對了！“
# 猜錯的話 要告訴他 比答案大/小


import random

r = random.randint(1, 100)  #隨機整數, r = 答案


while True:                 #無限巡迴
    num = input('請猜數字從1到100 Guess a number between 1 and 100:')
    num = int(num)
    if num == r:
        print('你猜中了！You are right!')
        break
    elif num > r:
        print('比答案大 Too big!')
    elif num < r:
        print('比答案小 Too small!')

