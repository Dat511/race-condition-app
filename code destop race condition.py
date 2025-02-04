import threading
import tkinter as tk
import random

# Biến đếm toàn cục
counter = 0
lock = threading.Lock()  # Dùng Lock để tránh race condition

def increment_counter(limit):
    global counter
    for _ in range(limit):
        with lock:
            counter += 1

def start_counting():
    global counter
    counter = 0  # Reset giá trị trước khi bắt đầu

    # Giới hạn ngẫu nhiên số vòng lặp của mỗi luồng (800,000 - 1,000,000)
    limit1 = random.randint(800000, 1000000)
    limit2 = random.randint(800000, 1000000)

    # Tạo hai luồng chạy song song
    thread1 = threading.Thread(target=increment_counter, args=(limit1,))
    thread2 = threading.Thread(target=increment_counter, args=(limit2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Cập nhật giao diện với kết quả cuối cùng
    label_result.config(text=f"Counter: {counter}")

# Tạo giao diện với Tkinter
root = tk.Tk()
root.title("Randomized Counter Example")

btn_start = tk.Button(root, text="Start Counting", command=start_counting)
btn_start.pack(pady=10)

label_result = tk.Label(root, text="Counter: 0", font=("Arial", 16))
label_result.pack(pady=20)

root.mainloop()