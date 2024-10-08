# Toko buku
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Toko buku')
print('='*30)

HARGA_BUKU = 5000
HARGA_PENSIL = 3000
HARGA_PULPEN = 4000
HARGA_PENGHAPUS = 1000
HARGA_PENGSERUT = 2000
HARGA_PENGGARIS = 5000

buku = int(input('Masukan jumlah buku : '))
pensil = int(input('Masukan jumlah pensil : '))
pulpen = int(input('Masukan jumlah pulpen : '))
penghapus = int(input('Masukan jumlah penghapus : '))
pengserut = int(input('Masukan jumlah pengserut : '))
penggaris = int(input('Masukan jumlah penggaris : '))

ttl_buku = buku * HARGA_BUKU
ttl_pensil = pensil * HARGA_PENSIL
ttl_pulpen = pulpen * HARGA_PULPEN
ttl_penghapus = penghapus * HARGA_PENGHAPUS
ttl_penggaris = penggaris * HARGA_PENGGARIS

total = ttl_buku + ttl_pensil + ttl_pulpen + ttl_penghapus + ttl_penggaris
diskon = total * 12.5/100
bayar = total - diskon


print('Jumlah : ', total)
print('diskon : ', diskon)
print('Total : ', bayar, '\n')