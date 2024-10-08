# Inputan Perkalian
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Inputan Perkalian')
print('='*30)

jumlah_perkalian = int(input("\nMasukkan jumlah perkalian: "))

for i in range(1, jumlah_perkalian+1):
  for j in range(1, 3):
    hasil = i * j
    print(f"{j} x {i} = {hasil}", end="  ")
  print()