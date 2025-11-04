# Rosnena/algoritma-shorting-comparison

Perbandingan berbagai algoritma sorting menggunakan Python. Versi Rosnena.

## Deskripsi
Project ini mengimplementasikan beberapa algoritma sorting klasik dan membandingkan waktu eksekusinya pada dataset berukuran berbeda. Cocok untuk keperluan pembelajaran dan analisis kompleksitas.

## Cara pakai
1. Ekstrak repository.
2. (Opsional) Buat virtualenv dan install dependency: `pip install -r requirements.txt`
3. Jalankan perbandingan tanpa skip:
   `python app_fullcomparison_nskip.py`
4. Jalankan perbandingan dengan mekanisme skip (melewati algoritma O(n^2) pada dataset besar):
   `python app_fullcomparison_skip.py`

## Struktur
- app.py : CLI sederhana untuk menjalankan satu algoritma atau contoh
- app_fullcomparison_nskip.py : jalankan semua algoritma (tanpa skip)
- app_fullcomparison_skip.py : jalankan semua algoritma dengan skip threshold
- matplotlib.py : util plotting (opsional)
- requirements.txt
- LICENSE (MIT)
