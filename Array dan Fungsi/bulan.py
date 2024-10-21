# Menampilkan bulan dengan array
# Created by arsa
# 18-10-2024

bulan = ['januari',
         'februari',
         'maret',
         'april',
         'mei',
         'juni',
         'juli',
         'agustus',
         'september',
         'oktober',
         'november',
         'desember'
]
print(bulan[2])
print(bulan[9])
bulan[7] = 'august'
bulan[0] = 'january'
bulan.append('muharam')

i = 1
for j in bulan:
    print('Bulan ke', i, j)
    i = i+1