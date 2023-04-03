#BTVN 27/3/2023
#BT1: Làm lại form Add User
#Kiểm tra dữ liệu khi Administrator tạo người dùng mới
# - Username: Không rỗng, tối đa 30 ký tự, không có các ký tự đặc biệt như @, #, $, %
# - Password: Không rỗng, tối thiểu 8 ký tự, chứa 1 trong ký tự đặc biệt: @, #, $, %
# - Role: Không rỗng
# - Khi kiểm tra trong DB, username phải chưa tồn tại