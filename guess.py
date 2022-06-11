import random
number = random.randint(1, 100)


while True:
	r = input('請輸入數字')
	r = int(r)
	if r == number:
		print('終於猜對了')
		break
	elif r > number:
		print('比答案大')
	else:
		print('比答案小')


