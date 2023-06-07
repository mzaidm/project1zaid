pengambilan_produk = 1020000
jumlah_kendaraan = 6

if pengambilan_produk >= 1000000:
    if jumlah_kendaraan > 8:
        print("anda memenuhi syarat sebagai distributor di daerah ini. ")
    else:
        print("jumlah kendaraan anda tidak memenuhi syarat. ")
else:
    print("pengambilan produk anda tidak memenuhi syarat.")