#Program Dictionary

dict = {'Nama':['Alica Ayu Fitriani'],
        'Hobi':['Mendengarkan musik', 'membaca webtoon', 'menggambar'],
        'Sosmed':['Instagram: alicaaf_', 'Twitter: alicafitriani', 'Line: alicaaf_'],
        'Lagu Kesukaan':['Lie to Me', 'I Got You', 'April'],
        'Makanan Favorit':['Ice cream', 'semangka', 'martabak']}
print(dict)

#Mengubah hobi dan sosial media
dict['Hobi'][2] = ('badminton')
dict['Sosmed'][0] = ('Linkedln: Alica Ayu Fitriani')

#Menghapus dua makanan favorit
del dict['Makanan Favorit'][0:2]

#Menambah hobi
dict['Hobi'].append('menonton film')

print(dict)