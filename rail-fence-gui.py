import tkinter as tk
from tkinter import messagebox
import time
import threading
import random

# Rail Fence Cipher Encryption
def encrypt(data, depth):
    rows = ["" for _ in range(depth)]
    for i, char in enumerate(data):
        rows[i % depth] += char
    return ''.join(rows)

def show_shuffling_animation_with_dots(text_var, original_text, duration=2):
    start_time = time.time()
    dots = ["", ".", "..", "..."]  # Three dots animation cycle
    while time.time() - start_time < duration:
        shuffled = ''.join(random.sample(original_text, len(original_text)))
        dot_cycle = dots[int((time.time() * 4) % 4)]  # Rotate dots based on time
        text_var.set(f"{shuffled}{dot_cycle}")
        time.sleep(0.1)

def start_encryption():
    data = input_text.get()
    try:
        depth = int(depth_var.get())
        if not (2 <= depth <= 6):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 2 and 6 for depth.")
        return

    if not data:
        messagebox.showerror("Invalid Input", "Please enter some text to encrypt.")
        return

    # Start animation and encryption in a separate thread
    def process_encryption():
        show_shuffling_animation_with_dots(result_var, data)
        encrypted_data = encrypt(data, depth)
        result_var.set(encrypted_data)

    threading.Thread(target=process_encryption, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Rail Fence Cipher")

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

tk.Label(frame, text="Enter text to encrypt:").grid(row=0, column=0, sticky="w")
input_text = tk.Entry(frame, width=40)
input_text.grid(row=0, column=1, padx=10)

# Depth Selection
tk.Label(frame, text="Enter depth (2-6):").grid(row=1, column=0, sticky="w")
depth_var = tk.StringVar()
depth_entry = tk.Entry(frame, textvariable=depth_var, width=5)
depth_entry.grid(row=1, column=1, sticky="w")

# Encrypt Button
encrypt_button = tk.Button(frame, text="Encrypt", command=start_encryption)
encrypt_button.grid(row=2, columnspan=2, pady=10)

# Result Display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
