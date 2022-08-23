chieucao = float(input("Nhập chiều cao của cơ thể (đơn vị: m): "))
cannang = float(input("Nhập cân nặng của cơ thể (đơn vị: kg): "))
BMI = cannang/(chieucao*chieucao)
tinhtrangcothe = ''
if BMI < 16:
    tinhtrangcothe = 'Gầy cấp độ III'
elif 16 <= BMI < 17:
    tinhtrangcothe = 'Gầy cấp độ II'
elif 17 <= BMI < 18.5:
    tinhtrangcothe = 'Gầy cấp độ I'
elif 18.5 <= BMI < 25:
    tinhtrangcothe = 'Bình thường'
elif 25 <= BMI < 35:
    tinhtrangcothe = 'Béo phì cấp độ I'
elif 35 <= BMI < 40:
    tinhtrangcothe = 'Béo phì cấp độ II'
elif BMI >40:
    tinhtrangcothe = 'Béo phì cấp độ III'
print("Tình trạng cơ thể của con người là: ",tinhtrangcothe)