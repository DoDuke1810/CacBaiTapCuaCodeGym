num = int(input("Nhập số bất kì: "))
tinhchanle = ''
if num % 2 == 0:
    tinhchanle = 'chẵn'
elif num % 2 == 1:
    tinhchanle = 'lẻ'
else:
    print('Số nhập vào là số',tinhchanle)