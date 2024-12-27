# Menentukan triple pytagoras
# created by Arsa
# 15-12-2024

print('\n')
print('='*30)
print('Menentukan triple pytagoras')
print('='*30)

def cari_triple_pythagoras(limit):
    triple_pythagoras = []
    for a in range(1, limit):
        for b in range(a, limit):  # Mulai dari a untuk menghindari duplikasi (a, b) dan (b, a)
            c = (a**2 + b**2) ** 0.5
            if c.is_integer():  # Memeriksa apakah c adalah bilangan bulat
                triple_pythagoras.append((a, b, int(c)))
    return triple_pythagoras

# Tentukan batas angka untuk mencari triple Pythagoras
limit = int(input('Masukan limit pytagoras : '))
triple = cari_triple_pythagoras(limit)

print(f"Triple Pythagoras hingga {limit}:")
for t in triple:
    print(t)
