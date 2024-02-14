# #date and time (liblary)

# import datetime as dt
# hari_apa_ini = dt.date.today()

# print(f"hari apakah tanggal {hari_apa_ini} : {hari_apa_ini:%A}")

# # menulis secara manual
# tanggal_lahir = dt.date(2007,1,23)
# print(f"hari apakah tanggal {tanggal_lahir} : {tanggal_lahir:%A}")

# mesin pendeteksi hari lahir asy
import datetime as dt

print(5*"="+"Mesin pendeteksi hari lahir"+"="*5)
print(f"""    1. masukkan tahun lahir anda
    2. masukkan bulan lahir anda
    3. masukkan tanggal lahir anda
    !!!!! SEMUA INPUT MENGGUNAKAN ANGKA !!!!!  """)

# input
tahun = int(input("masukkan tahun lahir anda :"))
bulan = int(input("masukkan bulan lahir anda :"))
tanggal = int(input("masukkan tanggal lahir anda :"))

hasil = dt.date(tahun,bulan,tanggal)
print(f"jadi hari lahir anda : {hasil:%A}")

hari_ini = dt.date.today()
print(f"\ntanggal hari ini {hari_ini}")
umur = hari_ini - hasil
umur_tahun = umur.days // 365
umur_bulan = (umur.days // 365) / 30

print(f"jadi umur anda {umur_tahun} tahun")
print(f"jadi umur anda {umur_bulan} bulan")
