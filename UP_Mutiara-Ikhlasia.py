ulang = "yes"
while ulang == "yes":
    # di dalam while
    # perulangan
    print("=====Parkir Kampus=====")
    
    # input
    jeniskendaraan = input("Masukkan Jenis Kendaraan (motor/mobil/bus): ")
    lamaparkir = int(input("Masukkan Lama Parkir (jam): "))
    
    # percabangan pilih tarif
    if jeniskendaraan.lower() in ["motor", "sepeda motor"]:
        tarif = 2000
    elif jeniskendaraan.lower() == "mobil":
        tarif = 5000
    elif jeniskendaraan.lower() == "bus":
        tarif = 10000
    else:
        tarif = 0
        print("Jenis kendaraan tidak terdaftar!")
        
    # rumus hitung biaya
    biayaparkir = tarif * lamaparkir
    
    # percabangan cek biaya tambahan
    if lamaparkir > 5:
        biayatambahan = 5000
    else:
        biayatambahan = 0
        
    # rumus total pembayaran
    totalbayar = biayaparkir + biayatambahan
    
    # output
    print("Biaya Parkir :", biayaparkir)
    print("Biaya Tambahan :", biayatambahan)
    print("Total Pembayaran :", totalbayar)
    
    # while perulangan
    ulang = input("\nIngin Hitung Kendaraan Lagi (yes/no)?: ")

# diluar while
print("Anda Keluar")
print("Terimakasih Sudah Menggunakan Layanan Parkir!")
