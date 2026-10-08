# Pertemuan 06 Nested Loop Python

Nama: Laila Fadhilah
NIM: 2225250030
Kelas: 3A

## Tujuan

Pada pertemuan ini saya mempelajari penggunaan nested loop, pola, akumulasi, dan pencacahan dalam Python.

Tujuan latihan dan tugas ini adalah:

* memahami penggunaan loop bersarang atau nested loop;
* membuat pola menggunakan nested loop;
* menghitung jumlah nilai pada setiap baris;
* menghitung pasangan yang memenuhi suatu kondisi;
* menggunakan akumulator dan counter;
* membuat tabel perkalian menggunakan nested loop;
* melakukan pengujian dan tracing terhadap program.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan perintah:

```text
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

Program menerima input bilangan bulat positif `n`. Jika `n <= 0`, program meminta input kembali.

Program menggunakan nested loop. Loop luar digunakan untuk menentukan baris, sedangkan loop dalam digunakan untuk menentukan kolom.

Pada setiap perulangan:

* `hasil = i * j` digunakan untuk menghitung hasil perkalian.
* `total_baris` digunakan sebagai akumulator untuk menjumlahkan hasil pada setiap baris.
* `total_semua` digunakan sebagai akumulator untuk menjumlahkan seluruh hasil perkalian.
* `count_genap` digunakan sebagai counter untuk menghitung banyak hasil perkalian yang genap.

`total_baris` diinisialisasi di dalam loop luar agar kembali menjadi `0` pada setiap baris, sedangkan `total_semua` dan `count_genap` diinisialisasi sebelum nested loop.

## Hasil Pengujian

### Latihan 1 - Pasangan Indeks

Program menghasilkan pasangan `i` dari 1 sampai 3 dan `j` dari 1 sampai 4.

Hasil:

```text
(1,1)
(1,2)
(1,3)
(1,4)
(2,1)
(2,2)
(2,3)
(2,4)
(3,1)
(3,2)
(3,3)
(3,4)

Banyak pasangan = 12
```

Hasil yang diharapkan: 12 pasangan.
Hasil aktual: 12 pasangan.
Status: Sesuai.

### Latihan 2 - Pola Segitiga

Pengujian `n = 3`:

```text
*
* *
* * *
```

Hasil yang diharapkan: pola segitiga dengan 3 baris.
Hasil aktual: pola segitiga dengan 3 baris.
Status: Sesuai.

Pengujian juga dilakukan untuk `n = 1` dan `n = 5`.

### Latihan 3 - Jumlah Per Baris

Hasil pengujian:

```text
Jumlah baris 1 = 6
Jumlah baris 2 = 12
Jumlah baris 3 = 18
Jumlah baris 4 = 24
```

Hasil yang diharapkan: `6, 12, 18, 24`.
Hasil aktual: `6, 12, 18, 24`.
Status: Sesuai.

#### Tracing Latihan 3

| i | j | i × j | total_baris |
| - | - | ----: | ----------: |
| 1 | 1 |     1 |           1 |
| 1 | 2 |     2 |           3 |
| 1 | 3 |     3 |           6 |
| 2 | 1 |     2 |           2 |
| 2 | 2 |     4 |           6 |
| 2 | 3 |     6 |          12 |
| 3 | 1 |     3 |           3 |
| 3 | 2 |     6 |           9 |
| 3 | 3 |     9 |          18 |
| 4 | 1 |     4 |           4 |
| 4 | 2 |     8 |          12 |
| 4 | 3 |    12 |          24 |

### Latihan 4 - Menghitung Pasangan

Pengujian `n = 3` dilakukan untuk menghitung pasangan yang memenuhi kondisi:

```text
i + j <= n
```

#### Tracing Latihan 4

| i | j | i + j | Kondisi | count |
| - | - | ----: | ------- | ----: |
| 1 | 1 |     2 | Ya      |     1 |
| 1 | 2 |     3 | Ya      |     2 |
| 1 | 3 |     4 | Tidak   |     2 |
| 2 | 1 |     3 | Ya      |     3 |
| 2 | 2 |     4 | Tidak   |     3 |
| 2 | 3 |     5 | Tidak   |     3 |
| 3 | 1 |     4 | Tidak   |     3 |
| 3 | 2 |     5 | Tidak   |     3 |
| 3 | 3 |     6 | Tidak   |     3 |

Pasangan yang memenuhi kondisi:

```text
(1,1), (1,2), (2,1)
```

Hasil yang diharapkan: `3`.
Hasil aktual: `3`.
Status: Sesuai.

Pengujian juga dilakukan untuk `n = 2` dan `n = 5`.

### Tugas 3 - Tabel Perkalian dan Statistik

| Input | Hasil yang Diharapkan | Hasil Aktual          | Status |
| ----- | --------------------- | --------------------- | ------ |
| n = 1 | Total = 1, genap = 0  | Total = 1, genap = 0  | Sesuai |
| n = 2 | Total = 9, genap = 3  | Total = 9, genap = 3  | Sesuai |
| n = 3 | Total = 36, genap = 5 | Total = 36, genap = 5 | Sesuai |

Contoh hasil untuk `n = 3`:

```text
1   2   3   | jumlah baris = 6
2   4   6   | jumlah baris = 12
3   6   9   | jumlah baris = 18

Total seluruh hasil = 36
Banyak hasil genap = 5
```

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali dan loop dalam juga berjalan sebanyak `n` kali.

Jadi badan loop dalam berjalan:

```text
n × n = n² kali
```

Contohnya, untuk `n = 3`:

```text
3 × 3 = 9 kali
```

## Refleksi

Kesalahan nested loop yang perlu diperhatikan adalah penempatan inisialisasi akumulator.

`total_baris` harus diletakkan di dalam loop luar agar nilainya kembali menjadi `0` setiap kali masuk ke baris baru. Jika diletakkan di luar loop, jumlah setiap baris akan terus terakumulasi dan hasilnya menjadi tidak sesuai.

Selain itu, indentasi harus diperhatikan karena indentasi menentukan posisi suatu perintah di dalam nested loop atau di luar loop.
