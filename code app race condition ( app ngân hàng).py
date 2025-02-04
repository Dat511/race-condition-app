import threading
import time
import random

# Lớp mô phỏng tài khoản ngân hàng
class BankAccount:
    def __init__(self):
        self.balance = 0  # Số dư tài khoản ban đầu

    def deposit(self, amount):
        if random.random() > 0.1:  # 10% cơ hội bỏ qua giao dịch
            temp = self.balance  # Đọc số dư (Race Condition xảy ra ở đây)
            temp += amount        # Cộng thêm tiền
            time.sleep(0.0001)    # Giả lập độ trễ để tăng khả năng race condition
            self.balance = temp   # Ghi lại số dư mới (Race Condition có thể gây lỗi)

# Hàm cho mỗi luồng thực hiện việc gửi tiền
def make_deposits(account, amount, times):
    for _ in range(times):
        account.deposit(amount)

# Tạo tài khoản ngân hàng
account = BankAccount()

# Tạo hai luồng gửi tiền đồng thời vào cùng một tài khoản
thread1 = threading.Thread(target=make_deposits, args=(account, 5, 1000))  # Gửi 5$ x 1000 lần
thread2 = threading.Thread(target=make_deposits, args=(account, 5, 1000))  # Gửi 5$ x 1000 lần

# Bắt đầu các luồng
thread1.start()
thread2.start()

# Chờ các luồng kết thúc
thread1.join()
thread2.join()

# In kết quả cuối cùng
print(f"Số dư cuối cùng (Random < 10,000, có lỗi race condition): {account.balance}")