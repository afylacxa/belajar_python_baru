# Latihan percabangan

print(5*"=")
print("Kalkulator sederhana")
print(5*"=")

# input
num_1 = int(input("masukkan angka 1 anda: "))
num_2 = int(input("masukkan angka 2 anda: "))
oper = input("masukkan (+) / (-) / (*) / (/) : ")

if(oper == "+"):
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif(oper == "-"):
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif(oper == "*"):
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif(oper == "/"):
    print(f"{num_1} / {num_2} = {num_1 / num_2}")
else:
    print("operator yang anda masukkan tidak valid !!!")