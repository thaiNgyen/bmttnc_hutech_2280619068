#Hàm nhập vào một số nguyên
so = int(input("Nhập vào một số nguyên: "))
#Kiển tra số nguyên có phải là số chẵn hay không 
if so % 2 == 0:
    print(so, "Đây là số chẵn!")
#ngược lại nếu chia có phần dư đó là số lẽ
else:
    print(so, "Đây là số lẽ!")
 