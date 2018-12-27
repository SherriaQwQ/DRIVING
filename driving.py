country = input('請問您是哪國人？ ')
age = input('請輸入您的年齡： ')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('您可以考駕照囉！')
    else:
        print('您尚未具考駕照的資格喔！')
elif country == '美國':
    if age >= 16:
        print('您可以考駕照囉！')
    else:
        print('您尚未具考駕照的資格喔！')