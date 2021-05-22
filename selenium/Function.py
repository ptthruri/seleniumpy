# Định nghĩa Hàm add()
def add(a, b):
    sum = a + b
    return sum

# Nhập 2 số vào từ bàn phím
x = int(input("Nhập số thứ nhất:"))
y = int(input("Nhập số thứ hai:"))

# Gọi hàm add() vừa được định nghĩa ở trên
tong = add(x, y)

# In ra tổng vừa tính được
print("Tổng là: " + str(tong))


def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# Khi gọi hàm, nếu không truyền giá trị cho tham số, thì tham số sẽ tự động được gán giá trị mặc định