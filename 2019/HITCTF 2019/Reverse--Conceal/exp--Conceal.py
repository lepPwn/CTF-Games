a = '\x00' * 37
a = list(a)
a[0] = a[33] = '6'
a[1] = a[11] = a[28] = 'b'
a[2] = a[7] = a[15] = 'd'
a[3] = a[4] = 'e'
a[5] = a[16] = a[20] = a[24] = a[27] = a[30] = 'f'
a[6] = a[32] = '1'
a[8] = a[13] = a[18] = a[23] = '-'
a[9] = a[14] = '4'
a[10] = a[19] = a[21] = '9'
a[12] = '7'
a[17] = a[31] = '2'
a[22] = a[25] = 'a'
a[26] = a[35] = '8'
a[29] = a[34] = '3'
print ''.join(a)
