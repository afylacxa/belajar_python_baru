#menyambungkan string
a = 'adi'
b = 'samsul'
c = 'udinese'

hasil = a+b+c
print(hasil)

#menghitung panjang kata dengan len()
latter = 'inisepuluh'
print(len(latter))

# mencari sesuatu di string
print('a' in a) #hasilnya true jadi ada a di 'adi'

print('c' not in a)# hasilnya juga akan true karna c tidak ada di a 'adi'

#mengulang kata
# print("aduh "*15)
# print(15*"ada ")

# indexing (mengambil data dari string)
nama_lengkap = "muhammad asyraf"

print('index ke 0',a,':' + a[1])
print('index ke -1',a,':'+ a[-1])
print('index ke 1:4',nama_lengkap,':'+ nama_lengkap[1:4])
print('index ke 0,2,4,6,->',nama_lengkap,':'+ nama_lengkap[1:10:2])


#item paling kecil
print("paling kecil : "+ min(nama_lengkap))

#item paling besar
print("paling bwsar : "+ max(nama_lengkap))

ascii_code = ord(" ")
print('ASCII code untuk spasi adalah : ' + str(ascii_code))
data = 123
print('ASCII untuk data ini adalah : ' + chr(data))

#operator dalam bentuk method
data = "mahmudin bin usining ba"
jumlah = data.count("m")
print("jumlah o pada data adaldh: "+ str(jumlah)) #jadi jumlah nya hya 2, str untuk mengubah tipe data, dari integer ke string
