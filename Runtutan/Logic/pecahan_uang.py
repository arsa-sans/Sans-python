# Menentukan pecahan uang
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan pecahan uang')
print('='*30)

uang = int(input("\nMasukkan nilai uang (kelipatan 25): "))

# menggunakan operator // karena mengoprasikan bilangan terdekat bukan desimal
pecahan_1000 = uang // 1000
sisa = uang % 1000

pecahan_500 = sisa // 500
sisa = sisa % 500

pecahan_100 = sisa // 100
sisa = sisa % 100

pecahan_50 = sisa // 50
sisa = sisa % 50

pecahan_25 = sisa // 25

print(f'''\nPecahan Rp1000: {pecahan_1000} 
Pecahan Rp500 : {pecahan_500}
Pecahan Rp100 : {pecahan_100}
Pecahan Rp50 : {pecahan_50}
Pecahan Rp25 : {pecahan_25}
\n
''')