import threading
import tkinter as tk

# Biến đếm toàn cục
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000000):
        with lock:  # Đảm bảo thao tác tăng là an toàn
            counter += 1
def start_counting():
    global counter
    counter = 0  # Reset giá trị trước khi bắt đầu

    # Tạo hai luồng chạy song song
    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Cập nhật giao diện với kết quả cuối cùng
    label_result.config(text=f"Counter: {counter}")

# Tạo giao diện với Tkinter
root = tk.Tk()
root.title("Race Condition Example")

btn_start = tk.Button(root, text="Start Counting", command=start_counting)
btn_start.pack(pady=10)

label_result = tk.Label(root, text="Counter: 0", font=("Arial", 16))
label_result.pack(pady=20)

root.mainloop()
