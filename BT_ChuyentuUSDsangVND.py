import math
usd = int(input("Nhập số tiền USD cần đổi (đơn vị: USD): "))
tigia = int(input("Nhập tỉ giá VND/USD (đơn vị: đồng/dollar): "))
vnd = usd*tigia
print("Số tiền VND theo tỉ giá và số tiền USD nhập vào bên trên là: {sotien} đồng".format(sotien = vnd))
