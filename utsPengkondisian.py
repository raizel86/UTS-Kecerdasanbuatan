# untuk memasukan apakah nilai lebih besar atau kecil
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

# mengetahui besar nilai dengan teknik shorthand
nilai = int(input('Nilai Ujian : '))
print("Grade A") if nilai >= 90 else print("Grade B") if nilai >= 75 else print(
    "Grade C") if nilai >= 55 else print("Grade D")
