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
harga_produk = {
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
print("\n\t\t======= List Menu Barudak Ngopi =======\n")

#Menu
for i in data_produk:
 print("\t\t Menu : ", data_produk[i], "\tHarga : ", harga_produk[i],)

def buat_pesanan():
  data_menu = [
      ("americano", 15000),
      ("cappuccino", 17000),
      ("mochacico", 14000),
      ("espresso", 15500),
      ("latte", 12000),
      ("macchiato", 17500),
      ("affogato", 20000),
      ("cold Brew", 18000),
      ("kentang", 8000),
      ("churos", 5000),
      ("sosis", 5000),
      ("batagor", 10000),
      ("siomay", 10000),
      ("jus mangga", 5000),
      ("jus mambu", 5000),
      ("jus jeruk", 3000),
      ("jus alpukat", 8000),
      ("jus tomat", 5000)
   ]
  total_harga = 0

# memesan
  while True:
    try:
        pesan_barang = input("\nMasukkan nama menu yang ingin dipesan ('selesai' untuk mengakhiri): ")
        if pesan_barang == "selesai":
          break

        for data_barang, data_harga in data_menu:
          if data_barang == pesan_barang:
            total_harga += data_harga
    except ValueError:
      print("Menu tidak terssedia\n")


# pembayaran
  bayar = input("\nLanjut Pembayaran?[y/n] ")
  if bayar == "y" or bayar == "Y":
      print("\n==================== Metode Pembayaran ====================")
  elif bayar == "cancel" or bayar == "N" or bayar == "n":
    print("Terimakasih telah berkunjung\n")
    while True:
      buat_pesanan()
  for i in metode_payment:
    print("Id : ", i , "\t Metode Pembayaran : ", metode_payment[i])
  pilih_metode = int(input("Pilih Metode Pembarayan : "))
  if pilih_metode not in metode_payment:
    print("Metode pembayaran tidak tersedia\n")
    while True:
      pilih_metode = int(input("Pilih Metode Pembarayan : "))
      if pilih_metode in metode_payment:
        break

    

# konfirmasi
  if pilih_metode in metode_payment:
    nama_pemesan = (input("Atas Nama : "))
    print("\nAtas Nama : ", nama_pemesan)
    print("Metode Pembayaran : ", metode_payment[pilih_metode])
    print("Total harga: Rp.",total_harga)
  konfirmasi = input("Apakah Anda Ingin Melanjutkan Pembayaran?[y/n] ")
  if konfirmasi == "Y" or konfirmasi == "y":
    print("Anda berhasil melakukan pemesanan, mohon tunggu sebentar!\n")
    while True:
      buat_pesanan()
  elif konfirmasi == "cancel" or konfirmasi == "N" or konfirmasi == "n":
    print("Terimakasih telah berkunjung\n")
    while True:
      buat_pesanan()
buat_pesanan()