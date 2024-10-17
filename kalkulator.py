import tkinter as tk

# Fungsi untuk melakukan operasi matematis
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "Tambah":
            result = num1 + num2
        elif operation == "Kurang":
            result = num1 - num2
        elif operation == "Kali":
            result = num1 * num2
        elif operation == "Bagi":
            result = num1 / num2
        else:
            result = "Operasi tidak dikenali"
        
        label_result.config(text="Hasil: " + str(result))
    except ValueError:
        label_result.config(text="Masukkan angka yang valid")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Membuat elemen GUI
label1 = tk.Label(root, text="Angka 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Angka 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Tombol untuk operasi
button_add = tk.Button(root, text="Tambah", command=lambda: calculate("Tambah"))
button_add.pack()

button_subtract = tk.Button(root, text="Kurang", command=lambda: calculate("Kurang"))
button_subtract.pack()

button_multiply = tk.Button(root, text="Kali", command=lambda: calculate("Kali"))
button_multiply.pack()

button_divide = tk.Button(root, text="Bagi", command=lambda: calculate("Bagi"))
button_divide.pack()

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="Hasil: ")
label_result.pack()

# Menjalankan program
root.mainloop()
