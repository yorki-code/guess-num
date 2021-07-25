# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話, 印出 "終於猜對了!"
# 猜錯的話, 要告訴他, 比答案大/小

import random
start = input('請決定隨機數字起始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)

n = random.randint(start, end)
count = 0   # 計數的變數
while True:
    count += 1  # count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == n:
        print('你猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > n:
        print('比答案大')
    elif num < n:
        print('比答案小')
    print('這是你猜的第', count, '次')
      
