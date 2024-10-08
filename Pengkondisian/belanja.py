# Belanja minimal 200k
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Belanja minimal 200k')
print('='*30)

BARANG_1 = 30000
BARANG_2 = 20000
BARANG_3 = 40000
BARANG_4 = 60000


barang_1 = int(input('Masukan jumlah barang pertama : '))
barang_2 = int(input('Masukan jumlah barang keuda : '))
barang_3 = int(input('Masukan jumlah barang ketiga : '))
barang_4 = int(input('Masukan jumlah barang keempat : '))


ttl_brg1 = barang_1 * BARANG_1
ttl_brg2 = barang_2 * BARANG_2
ttl_brg3 = barang_3 * BARANG_3
ttl_brg4 = barang_4 * BARANG_4

total = ttl_brg1 + ttl_brg2 + ttl_brg3 + ttl_brg4
diskon = total * 7.5/100
bayar = total - diskon

if total < 200000 :
    print(f'Total harga : {total}')
else :
    print('Anda mendapat diskon sebanyak 7.5% :', bayar)