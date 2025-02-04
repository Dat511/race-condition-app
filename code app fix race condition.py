import threading
import time

# Lớp mô phỏng tài khoản ngân hàng
class BankAccount:
    def __init__(self):
        self.balance = 0  # Số dư tài khoản ban đầu
        self.lock = threading.Lock()  # Thêm Lock để tránh race condition

    def deposit(self, amount):
        with self.lock:  # Đảm bảo chỉ một luồng thực hiện cập nhật balance
            temp = self.balance
            temp += amount
            time.sleep(0.0001)  # Giả lập độ trễ để kiểm tra race condition
            self.balance = temp

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
print(f"Số dư cuối cùng (chính xác 10,000): {account.balance}")