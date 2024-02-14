# and, or, not, xor

#OR
print("=========OR") # jadi kalau or bila salah satu true maka hasilnya akan true
a = False
b = False
hasil = a or b
print(a, "OR", b, "=", hasil)

a = True
b = False
hasil = a or b
print(a, "OR", b, "=", hasil)

a = False
b = True
hasil = a or b
print(a, "OR", b, "=", hasil)

a = True
b = True
hasil = a or b
print(a, "OR", b, "=", hasil)

#NOT
print("=========NOT")
a = True
hasil = not a
print(a,'not =', hasil)

#AND hanya akan menjadi true ketika kedua inputnya true
print("=========AND")
a = False
b = False
hasil = a and b
print(a, "and", b, "=", hasil)

a = True
b = False
hasil = a and b
print(a, "and", b, "=", hasil)

a = False
b = True
hasil = a and b
print(a, "and", b, "=", hasil)

a = True
b = True
hasil = a and b
print(a, "and", b, "=", hasil)

#XOR 
print("=========XOR")
a = False
b = False
hasil = a ^ b
print(a, "^", b, "=", hasil)

a = True
b = False
hasil = a ^ b
print(a, "^", b, "=", hasil)

a = False
b = True
hasil = a ^ b
print(a, "^", b, "=", hasil)

a = True
b = True
hasil = a ^ b
print(a, "^", b, "=", hasil)