# width and multiline

# Data
data_nama = "ucup de jummer"
data_umur = 18
data_tinggi = 154.2
data_nomor_sepatu = 43

#string
data_string = f"nama = {data_nama}m umur{data_umur}, data tinggi = {data_tinggi} dan data no sepatu {data_nomor_sepatu}"
print(5*'='+"data string"+"="*5)
print(data_string)

# string multi line
data_string = f"nama = {data_nama},  \numur{data_umur}, \ndata tinggi = {data_tinggi}, \ndan data no sepatu {data_nomor_sepatu}"
print(5*'='+"data string"+"="*5)
print(data_string)

#string multiline """
data_nama = "ucup"
data_string = f""" nama = {data_nama:>19},
 umur   = {data_umur},
 tinggi = {data_tinggi},
 sepatu = {data_nomor_sepatu}"""
print(5*'='+"data string"+"="*5)
print(data_string)