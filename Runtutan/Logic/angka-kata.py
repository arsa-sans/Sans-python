# Mengubah angka menjadi kata kata
# created by Arsa
# 15-12-2024

print('\n')
print('='*30)
print('Mengubah angka menjadi kata kata')
print('='*30)

def angka_ke_kata(angka):
    satuan = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
    belasan = ["Sepuluh", "Sebelas", "Dua belas", "Tiga belas", "Empat belas", "Lima belas", "Enam belas", "Tujuh belas", "Delapan belas", "Sembilan belas"]
    puluhan = ["", "", "Dua puluh", "Tiga puluh", "Empat puluh", "Lima puluh", "Enam puluh", "Tujuh puluh", "Delapan puluh", "Sembilan puluh"]
    
    if angka == 0:
        return "Nol"
    
    kata = []
    
    if angka >= 1000:
        ribuan = angka // 1000
        kata.append(satuan[ribuan] + " Ribu")
        angka = angka % 1000
    
    if angka >= 100:
        ratusan = angka // 100
        kata.append(satuan[ratusan] + " Ratus")
        angka = angka % 100
    
    if angka >= 10:
        if angka < 20:
            kata.append(belasan[angka - 10])
            angka = 0
        else:
            puluhan_angka = angka // 10
            kata.append(puluhan[puluhan_angka])
            angka = angka % 10
    
    if angka > 0:
        kata.append(satuan[angka])
    
    return " ".join(kata)

angka = int(input("Masukkan angka positif: "))
print(f"{angka} dalam kata-kata adalah: {angka_ke_kata(angka)}")
