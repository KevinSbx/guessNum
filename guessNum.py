# 產生一個蕤機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話印出 "你猜對了"
# 猜錯的話 印出 "比答案大/小"

import random
start = int(input("請決定隨機數字範圍起始值: "))
end = int(input("請決定隨機數字範圍結束值: "))
 
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = int(input("請猜數字: "))
	if num == r:
		print("你猜中了")
		print("這是你猜的第", count, "次")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("這是你猜的第", count, "次")