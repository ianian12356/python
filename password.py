password1 = 'a123456'
password2 = input('請輸入密碼:')

i = 2
while i > 0:
	if password2 == password1:
		print('登入成功')
		break
	else:
		print('密碼錯誤!還有', i, '次機會')
		password2 = input('請輸入密碼:')
		i = i - 1


