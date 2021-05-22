num_int = 123
num_flo = 1.23
num_str = "456"

num_new = num_int + num_flo

print("Kiểu dữ liệu của num_int:", type(num_int))
print("Kiểu dữ liệu của num_flo:", type(num_flo))


num_str = int(num_str)
# Ép kiểu DL từ str sang int
print("Kiểu dữ liệu của num_str:",type(num_str))

print("Giá trị của num_new:", num_new)
print("Kiểu dữ liệu của num_new:", type(num_new))