# Program Kalkulator Sederhana

# Input dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Input operator aritmatika
operator = input("Masukkan operator (+, -, *, /): ")

# Menghitung hasil berdasarkan operator yang dipilih
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = float('inf')
else:
    hasil = "Operator tidak valid!"

# Menampilkan hasil
print("Hasil:", hasil)

