drive = input('開過車嗎?')
age = input('幾歲?')
age = int(age)

if drive == '有':
	if age >= 18:
		print('哈哈')
	else :
		prnt("甚麼鬼")
else :
	print('可憐') 