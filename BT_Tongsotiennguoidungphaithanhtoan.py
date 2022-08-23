num = int(input("Nhập vào giá tiền (đơn vị: $): "))
if num >= 150:
	print("Tổng số tiền phải trả: ", num - 50)
elif num >= 100:
	print("Tống số tiền phải trả: ", num - 25)
elif num >= 75:
	print("Tổng số tiền phải trả: ", num - 15)
else:
    print("Tổng số tiền phải trả: ", num)