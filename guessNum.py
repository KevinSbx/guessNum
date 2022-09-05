# 產生一個蕤機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話印出 "你猜對了"
# 猜錯的話 印出 "比答案大/小"

import random
 
r = random.randint(1, 100)
while True:
	num = int(input("請猜數字: "))
	if num == r:
		print("你猜中了")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")