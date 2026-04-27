import qrcode
from PIL import Image

import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter text to generate QR code.")
        return

    qr = qrcode.make(data)
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png", 
        filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
    )
    
    if file_path:
        qr.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")


root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")


label = tk.Label(root, text="Enter text or URL:")
label.pack(pady=10)


entry = tk.Entry(root, width=40)
entry.pack(pady=5)


button = tk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=10)

root.mainloop()

