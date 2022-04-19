print("Masukan 2 buah Nilai")
a = int(input('bilangan a : '))
b = int(input('bilangan b : '))
if a > b:
    print(a, " lebih besar dari ", b)
else:
    print(a, " Lebih kecil dari ", b)

# untuk menentukan bilangan ganjil dan genap
print("Menentukan Bilangan ganjil & genap")
bilangan = int(input('Masukan Bilangan: '))
print('nilai', bilangan, 'adalah bilangan',
      'genap' if (bilangan % 2 == 0) else 'ganjil')
