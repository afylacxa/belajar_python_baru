# Operator dalam bentuk methods
## merubah case dari string

#merubah semua ke uppercase
salam = "Halo kak"
print("salam biasa : "+salam)
print("salam biasa : "+salam.upper())
#UNTUK KE   lowercase
print("salam biasa : "+salam.lower())

## pengecekan dengan isX method
hasil = salam.islower() #hasilnya boolean
print("apakah salam is lower :" + str(hasil))
hasil = salam.isupper() #hasilnya boolean
print("apakah salam is upper :" + str(hasil))

#isalpha() <-- ini mengecek semua huruf
#isalnum() <-- huruf dan angka
#isdecimal() <-- angka saja
#isspaca() <--  spasi, tab, newline
#istitle() <--Semua kata untuk huruf kapital

## startswith() dan endswith()
cek_start = "uninese barbosa".startswith("uninese")
print('start : ' + str(cek_start))
cek_end = "uninese barbosa".endswith("barbosse")
print('start : ' + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu'] # namanya list
gabungan =" janji ".join(pisah) # string adalah sebagai penyambungnya
print(gabungan)

gabung = "cobaehmjanjiehmsamaehmaku"
print(gabung.split('ehm'))

## alokasi karakter ljust() rjust center() (adalah jarak,pakai apa)
tengah = "mahmudin udinise".center(28,"=")
print(tengah)

# kebalikannya strip

ubah = tengah.strip("=")
print(ubah)

#method tidak hanya ini masih banyak jenis nya jadi bisa cari di internet