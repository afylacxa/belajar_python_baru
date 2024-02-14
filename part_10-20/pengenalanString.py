# String


#  1. Cara membuat String

'''
    1. Dengan menggunakan single qoute '...'
    2. Dengan menggunakan double qoute "..."
'''

data = 'ini single qoute'
print(data)
data = "ini double qoute"
print(data)

# Menggunakan tanda \

# menjadikan tanda ' jadi string
print('hari ini adalah hari jum\'at ')

# backslash \ dengan double \\ 
print('c:\\helui')

# tab \t
print('udin \t \t mahmud')

# backspace \b
print('udin \bmahmud')

# newline \n
# print('ini baris pertama.\nini baris kedua.')
# print('ini baris pertama.\rini baris kedua.')
print('ini baris pertama.\r\nini baris kedua.')

# string literal atau raw

# hati hati dengan ini
print('c:\\new folder') # ini salah penulisan path nya

    # dengan raw
print(r'c:\\new folder')

# multiline literal string
print("""
Ucup kelas : 2
adin kelas : 4  
""")

# multiline raw literal string
print(r"""
uindadk /t : kanan
uindadk /r : kanan
""")