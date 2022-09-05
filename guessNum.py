# 產生一個蕤機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話印出 "你猜對了"
# 猜錯的話 印出 "比答案大/小"

import random
 
r = random.randint(1, 100)
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