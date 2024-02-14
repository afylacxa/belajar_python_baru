# format string



## contoh generic
nama = "asyraf"
str = "hai" + nama


print(str)

## contoh format string
format_str = f"hai {nama}"
print(format_str)

#angka 
angka = 2007
format_str = f"saya lahir tahun : {angka}"
print(format_str)

#boolean
boolean = True
format_str = f"ini adalah nilai boolean : {boolean}"
print(format_str)

#bilangan bulat
angka = 17
format_str = f"bilangan bulat : {angka:d}"
print(format_str)

#bilangan ribuan
angka = 15000
format_str = f"bilangan ribuan : {angka:,}" # tanda : dan , akan otomatis dari 15000 ke 15,000
print(format_str)

#bilangan decimal float
angka = 1789.569
format_str = f"bilangan decimal : {angka:.2f}" # maka yang di tampilkan hanya 2 angka di belakang koma
print(format_str)

#menampilkan leading zero / didepan
angka = 141.51123
format_str = f"bilangan decimal : {angka:08.2f}"
print(format_str)

#menampikan angka + / -
angka = + 17
angka_minus = - 27
format_str = f"bilangan positif : {angka:+d}"
print(format_str)
format_str = f"bilangan negatif : {angka_minus:+d}"
print(format_str)

#format persen 
persentase = 0.043
format_persen = f"persennya : {persentase:.2%}"
print(format_persen)

#didalam kurung kurawal juga misa melakukan operasi aritmatika
harga = 15000
jumlah = 5
print(f"jumlah dari harga {jumlah} adalah Rp.{harga*jumlah}")


#format angka lain speerti binary, octal ,hexadecimal
angka = 156

format_bin = f"decimal {bin(angka)}"
print(format_bin)
format_oct = f"octal {oct(angka)}"
print(format_oct)
format_hex = f"hexadecimal {hex(angka)}"
print(format_hex)