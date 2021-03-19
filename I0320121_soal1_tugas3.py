#List nama teman
listnama = ['Iffa', 'Retno', 'Anisa', 'Uly', 'Sylvia', 'Dea', 'Rafi', 'Afnan', 'Alya', 'Rahmat']

#Menampilkan list index nomor 4, 6, 7
print("List nama teman pada index nomor 4, 6, 7:", listnama[4],',',listnama[6],',',listnama[7])

#Mengganti nama teman pada list 3, 5, 9
listnama[3] = 'Raysa'
listnama[5] = 'Tsania'
listnama[9] = 'Mira'


#Menambahkan nama teman
listnama.extend(['Yuki', 'Salma'])

#Menampilkan semua teman dengan perulangan
print("\nList nama teman:")
teman = 0
for data in range(0,12):
    print(listnama[teman])
    teman = teman+1

#Menampilkan panjang list nama teman
print("\nPanjang list adalah", len(listnama))
