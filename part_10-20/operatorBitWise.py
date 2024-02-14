#operasi bitwise biner binary
a = 5
b = 7

# bitwise OR (|)
c = a | b
print('\n =====OR====')
print('nilai',a,' , binary :',format(a,'08b'))
print('nilai',b,' , binary :',format(b,'08b'))
print('----------------------(|)')
print('nilai',c,' , binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n =====AND====')
print('nilai',a,' , binary :',format(a,'08b'))
print('nilai',b,' , binary :',format(b,'08b'))
print('----------------------(&)')
print('nilai',c,' , binary :',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n =====XOR====')
print('nilai',a,' , binary :',format(a,'08b'))
print('nilai',b,' , binary :',format(b,'08b'))
print('----------------------(^)')
print('nilai',c,' , binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n =====not====')
print('nilai',c,' , binary :',format(c,'08b'))
print('----------------------(~)')

# shifting

# shifting right
c = a >> 1
print('\n =====>>====')
print('nilai',a,' , binary :',format(a,'08b'))
print('nilai',c,' , binary :',format(c,'08b'))

# shifting left
c = a << 1
print('\n =====<<====')
print('nilai',a,' , binary :',format(a,'08b'))
print('nilai',c,' , binary :',format(c,'08b'))