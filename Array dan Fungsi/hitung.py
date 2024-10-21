import time

# Menghitung detik
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Menghitung detik')
print('='*30)

def hitung_waktu():
    jumlah_detik = int(input("Masukkan jumlah detik: "))
    for detik in range(jumlah_detik, 0, -1):
        print(detik, end='\r')
        time.sleep(1)
    print("Waktu habis!")

hitung_waktu()