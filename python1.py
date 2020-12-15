## membuat aplikasi belanja 1

# Berikan 2 ke variable apple_price 
apple_price = 2

# Berikan 5 ke variable count 
count = 5

# Berikan hasil dari apple_price * count ke variable total_price 
total_price = apple_price * count

# Dengan menggunakan variable count, cetak 'Anda akan membeli .. apel'
print('Anda akan membeli ' + str(count) + ' apel')

# Dengan menggunakan variable total_price, cetak 'Harga total adalah .. dolar'
print('Harga total adalah ' + str(total_price) +  ' dolar')


## membuat aplikasi belanja 2
apple_price = 2

# Terima jumlah apel dengan menggunakan input(), dan berikan hasilnya ke variable input_count 
input_count = input('Mau berapa apel?: ')

# Ubah variable input_count ke integer, dan berikan hasilnya ke variable count 
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

## membuat aplikasi belanja 3

apple_price = 2
# Berikan 10 ke variable money 
money = 10

input_count = input('Mau berapa apel?: ')
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

# Tambahkan control flow berdasarkan perbandingan antara money dan total_price
if money > total_price :
    sisa = money - total_price
    print('Anda telah membeli ' + str(count) + ' apel')
    print('Uang Anda tinggal ' + str(sisa) + ' dolar')
elif money == total_price :
    print('Anda telah membeli ' + str(count) + ' apel')
    print('Dompet Anda kosong')
else :
    print('Uang Anda tidak mencukupi')
    print('Anda tidak dapat membeli apel sebanyak itu')