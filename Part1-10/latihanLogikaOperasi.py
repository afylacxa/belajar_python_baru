# ++++++3-----10++++++
# userInput = float(input('masukkan angka yang kurang dari 3 \n atau \n lebih dari 10 = '))

# isKurangDari3 = userInput < 3
# print("Kurang dari 3 =",isKurangDari3)

# isLebihDari10 = userInput > 10
# print("Lebih dari 10 =",isLebihDari10)

# isFinaly = isKurangDari3 or isLebihDari10
# print("angka yang anda masukkan :",isFinaly)

# -----3++++++10----
userData = float(input("masukkan angka yang lebih dari 3 dan kurang dari 10 ="))
tData  = userData > 3
sData = userData < 10

print("lebih dari 3 :", tData,"kurang dari 10 :", sData)

hData = sData and tData
print('angka yang anda masukkan :',hData)