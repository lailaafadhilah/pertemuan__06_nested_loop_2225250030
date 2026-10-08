# Latihan 4 - Menghitung Pasangan
# Loop luar dan loop dalam menghasilkan seluruh pasangan i dan j.
# Counter bertambah jika i + j <= n.

n = int(input("n: "))
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")