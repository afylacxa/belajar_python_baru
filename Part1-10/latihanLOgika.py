# ----0+++++5-----8++++++11------
dataUser = float(input("masukkan data yang ----0+++++5-----8+++++++11------ : "))

# -----0++++++
steapUser1 = dataUser > 0
print("----0++++",steapUser1)

# +++++5-----
steapUser2 = dataUser < 5
print("++++++5-----",steapUser2)

# ------8++++++
steapUser3 = dataUser > 8
print("----8++++",steapUser3)
# ++++++11-----
steapUser4 = dataUser < 11
print("++++++11-----",steapUser4)

# Proses untuk melakukan validasi yang ke 1
hasil1 = steapUser1 and steapUser2
hasil2 = steapUser3 and steapUser4

print("----0++++5----",hasil1)
print("----8++++11----",hasil2)

# Proses untuk melakukan validasi yang ke 2
hasilAkhir = hasil1 or hasil2

print('jadi anga yang kamu masukkan :',hasilAkhir)