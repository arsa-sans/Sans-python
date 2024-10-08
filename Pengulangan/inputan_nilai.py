# rumus nilai
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Inputan Nilai')
print('='*30)

nilai = []
jumlah = 0

while True:
    bilangan_str = input("Masukkan nilai (atau ketik 'selesai' untuk berhenti): ")
    if bilangan_str.lower() == 'selesai':
        break
    
    if not bilangan_str.isdigit():
        print("Input tidak valid. Silakan masukkan angka.")
        continue

    bilangan = float(bilangan_str)
    nilai.append(bilangan)
    jumlah += bilangan

if nilai:
    rata_rata = jumlah / len(nilai)
    print("Jumlah nilai:", jumlah)
    print("Rata-rata nilai:", rata_rata)
    print('\n')
else:
    print("Anda belum memasukkan nilai.")
    print('\n')

print('\n')