# Latihan 2 - Pola Segitiga
# Loop luar menentukan jumlah baris.
# Loop dalam menentukan jumlah bintang pada setiap baris.

n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()