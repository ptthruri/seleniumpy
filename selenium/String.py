print("Hello")
# Trong Python có thể dùng "" như là ''

str1 = """Dong thu 1
Dong thu 2
Dong thu 3
Dong thu 4
Dong thu 5"""
print(str1)
# Nếu dùng 3 dấu nháy liên tiếp thì có thể tạo một chuỗi có nhiều dòng

str2 = "HELLO"
print(str2[:])
print(str2[0:])
print(str2[:5])
print(str2[:3])
print(str2[0:2])
print(str2[1:4])
# trước dấu : vị trí bắt đầu lấy trong mảng
# sau dấu : lấy cho tới vị trí đó thì dừng không lấy nữa

a = " Hello World!"
print(len(a))
# Trả về chiều dài của chuỗi

print(a.strip())
#Nếu bạn muốn xóa khoảng trắng đầu và cuối, sử dụng .strip():
#Nếu bạn muốn xóa tất cả các khoảng trắng, sử dụng  .replace():
#Nếu bạn muốn xóa các không gian trùng lặp, sử dụng .split():

print(a.lower())
# Trả về một chuỗi chữ thường

print(a.upper())
# Trả về một chuỗi chữ hoa

print(a.replace("l", "t"))
# Thay thế tất cả cách chữ ở "" số 1 bằng chữ ở "" số 2

print(a.split(","))
# Tách chuỗi thành các chuỗi con

x = "python" in str1
print(x)
# Kiểm tra xem cụm từ "python" có tồn tại trong chuỗi sau không

a = "Hello "
b = "Python "
c = a + b
print(c)
# Nối hai chuỗi

txt = "Xin chao, toi la {}, {} tuoi, den tu {}"
print(txt.format("Nam", 22, "Ha Noi"))
# Sử dụng format có thể nối chữ , số vào một chuỗi