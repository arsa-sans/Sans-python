#data produk
data_produk = {
    1.1: "Americano",
    1.2: "Cappuccino",
    1.3: "Mochacino",
    1.4: "Espresso",
    1.5: "Latte  ",
    1.6: "Macchiato",
    1.7: "Affogato",
    1.8: "Cold Brew",
    
    2.1: "Kentang",
    2.2: "Churos",
    2.3: "Sosis ",
    2.4: "Batagor",
    2.5: "Siomay",
    
    3.1: "Jus Mangga",
    3.2: "Jus Jambu",
    3.3: "Jus Jeruk",
    3.4: "Jus Alpukat",
    3.5: "Jus Tomat",
}


#harga produk
harga = {
    1.1: 15000,
    1.2: 17000,
    1.3: 14000,
    1.4: 15500,
    1.5: 12000,
    1.6: 17500,
    1.7: 20000,
    1.8: 18000,

    2.1: 8000,
    2.2: 5000,
    2.3: 5000,
    2.4: 10000,
    2.5: 10000,
    
    3.1: 5000,
    3.2: 5000,
    3.3: 3000,
    3.4: 8000,
    3.5: 5000,
}


metode_payment = {
    1: "OVO",
    2: "GoPay",
    3: "Tunai",
}


#judul menu
print("\n\t\t========== List Menu Barudak Ngopi ==========\n")


#Menu
for i in data_produk:
    print("\tId Produk : ", i, "\t Menu : ", data_produk[i], "\tHarga : ", harga[i])


#Memesan
while True:
 mau_beli = input('\nMau pesan?[y/n] ')
 if mau_beli == "y" :
     pilih_id = float(input('\nPilih Id Product : '))
     if pilih_id in data_produk:
         pilih_beli =  input("Lanjut Memesan[y/n] ? ")

#pembayaran
         if pilih_beli == "Y" or pilih_beli == "y":
             print("\n==================== Metode Pembayaran ====================")
         elif pilih_beli == "N" or pilih_beli == "n":
             print("Terimakasih Telah Berkunjung\n")
             break
         for i in metode_payment:
          print("Id : ", i , "\t Metode Pembayaran : ", metode_payment[i])
         pilih_metode = int(input("Pilih Metode Pembarayan : "))

#konfirmasi
         if pilih_metode in metode_payment:
          nama_pemesan = (input("Atas Nama : "))
          print("\nAtas Nama : ", nama_pemesan)
          print("Produk : ", data_produk[pilih_id])
          print("Harga : ", harga[pilih_id])
          print("Metode Pembayaran : ", metode_payment[pilih_metode])
          konfirmasi = input("Apakah Anda Ingin Melanjutkan Pembayaran ?[y/n] ")
          if konfirmasi == "Y" or konfirmasi == "y":
             print("Anda berhasil melakukan pemesanan, mohon tunggu sebentar!\n")
          if konfirmasi == "N" or konfirmasi == "n":
             print("Terimakasih Telah Berkunjung\n")
             break
          else:
             pass
         else:
          print("Metode pembayaran tidak tersedia")
     else:
         print("Produk tidak tersedia")
 elif mau_beli == "n":
    print("Terimakasih Telah Berkunjung\n")
    break