# #1-masala
# fruits = ['olma', 'banan', 'uzum']

# fruits.append('nok')

# print(fruits)

# print(len(fruits))

# print('olma' in fruits)

# print(fruits.index('banan'))


# #2-msala
# colors = ['qizil', 'yashil', 'ko\'k']

# colors.append('sariq')
# print(colors)

# colors.sort()
# print(colors)

# print(len(colors))

# print('yashil' in colors)


# #3-masala
# cities = ['Toshkent', 'Samarqand', 'Buxoro']

# cities.append('Xiva')
# print(cities)

# print(cities.index('Samarqand'))

# print(len(cities))

# cities.sort()
# print(cities)


# #4-masala
# numbers = [5, 2, 8, 1]

# numbers.append(10)
# print(numbers)

# numbers.sort()
# print(numbers)

# print(len(numbers))

# print(2 in numbers)


# #5-masala
# animals = ['mushuk', 'it', 'qush']

# animals.append('baliq')
# print(animals)

# animals.sort()
# print(animals)

# print(animals.index('it'))

# print(len(animals))


# #6-masala
# fruits = ['olma', 'banan', 'uzum', 'nok']

# fruits.append('kivi')
# print(fruits)

# print(fruits.remove('banan'))

# print(fruits.insert(3, 'shaftoli'))

# fruits.sort()
# print(fruits)

# print(len(fruits))

# print(fruits.index('olma'))

# print('kivi' in fruits)


# # print(sorted(reversed=True))

# copied_fruits = fruits.copy()
# copied_fruits.append('ananas')

# print('Asl mevalar ro\'yxati:', fruits)
# print('Nusxa olingan mevalar ro\'yxati:', copied_fruits)


# #7-masala
# menu = ['osh', "lag'mon", 'shashlik', 'somsa']

# menu.extend(['manti', 'norin'])
# print(menu)

# menu.remove('lag\'mon')
# print(menu)

# print(menu.sort())

# print(len(menu))

# print(menu.index('osh'))

# print(menu.count('somsa'))

# print('manti' in menu)

# copied_menu = menu.copy()
# copied_menu.append('qozon kabob')

# print('Asl menyu:', menu)
# print('Nusxa olingan menyu:', copied_menu)


# #8-masala
# Boshlang'ich ro'yxat
cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Xiva']
print("Boshlang'ich ro'yxat:", cities)

# 1. Ro'yxat boshiga 'Andijon' qo'shing
cities.insert(0, 'Andijon')
print("1. 'Andijon' qo'shildi:", cities)

# 2. 'Xiva' ni ro'yxatdan olib tashlang
cities.remove('Xiva')
print("2. 'Xiva' o'chirildi:", cities)

# 3. 'Samarqand' ning indeksini toping
index_samarqand = cities.index('Samarqand')
print("3. 'Samarqand' ning indeksi:", index_samarqand)

# 4. Ro'yxatni alifbo tartibida tartiblang
cities.sort()
print("4. Alifbo tartibida:", cities)

# 5. Ro'yxatning uzunligini toping
length = len(cities)
print("5. Ro'yxat uzunligi:", length)

# 6. Ro'yxatda 'Buxoro' mavjudligini tekshiring
is_buxoro = 'Buxoro' in cities
print("6. 'Buxoro' mavjudmi?:", is_buxoro)

# 7. Oxirgi shaharni o'chiring
last_city = cities.pop()
print("7. O'chirilgan shahar:", last_city)
print("   Qolgan ro'yxat:", cities)

# 8. Ro'yxatni teskari tartibda tartiblang
cities.sort(reverse=True)
print("8. Teskari tartibda:", cities)

# 9. Ro'yxatni nusxalang va nusxaga 'Farg'ona' qo'shing
cities_copy = cities.copy()
cities_copy.append("Farg'ona")
print("9. Nusxa ('Farg'ona' qo'shilgan):", cities_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", cities)
print("    Nusxa ro'yxat:", cities_copy)


# #9-masala
# Boshlang'ich ro'yxat
students = ['Ali', 'Vali', 'Sardor', 'Aziz']
print("Boshlang'ich ro'yxat:", students)

# 1. Ro'yxatga 'Jamshid' ni oxiriga qo'shing
students.append('Jamshid')
print("1. 'Jamshid' qo'shildi:", students)

# 2. 'Sardor' ni ro'yxatdan olib tashlang
students.remove('Sardor')
print("2. 'Sardor' o'chirildi:", students)

# 3. 'Vali' dan oldin 'Diyor' qo'shing
index_vali = students.index('Vali')
students.insert(index_vali, 'Diyor')
print("3. 'Diyor' qo'shildi:", students)

# 4. Ro'yxatni alifbo tartibida tartiblang
students.sort()
print("4. Alifbo tartibida:", students)

# 5. 'Aziz' ning indeksini toping
index_aziz = students.index('Aziz')
print("5. 'Aziz' ning indeksi:", index_aziz)

# 6. Ro'yxatda 'Diyor' mavjudligini tekshiring
is_diyor = 'Diyor' in students
print("6. 'Diyor' mavjudmi?:", is_diyor)

# 7. Oxirgi talabani o'chiring
last_student = students.pop()
print("7. O'chirilgan talaba:", last_student)
print("   Qolgan ro'yxat:", students)

# 8. Ro'yxatning uzunligini toping
length = len(students)
print("8. Ro'yxat uzunligi:", length)

# 9. Ro'yxatni nusxalang va nusxaga 'Nodir' qo'shing
students_copy = students.copy()
students_copy.append('Nodir')
print("9. Nusxa ('Nodir' qo'shilgan):", students_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", students)
print("    Nusxa ro'yxat:", students_copy)


# #10-masala
# Boshlang'ich ro'yxat
favorites = ['telefon', 'noutbuk', 'naushnik']
print("Boshlang'ich ro'yxat:", favorites)

# 1. Ro'yxatga 'planshet' qo'shing
favorites.append('planshet')
print("1. 'planshet' qo'shildi:", favorites)

# 2. Ro'yxatga 'soat' qo'shing
favorites.append('soat')
print("2. 'soat' qo'shildi:", favorites)

# 3. Ro'yxatni alifbo tartibida tartiblang
favorites.sort()
print("3. Alifbo tartibida:", favorites)

# 4. Ro'yxatning uzunligini toping
length = len(favorites)
print("4. Ro'yxat uzunligi:", length)

# 5. 'noutbuk' ning indeksini toping
index_noutbuk = favorites.index('noutbuk')
print("5. 'noutbuk' ning indeksi:", index_noutbuk)

# 6. Ro'yxatda 'telefon' mavjudligini tekshiring
is_telefon = 'telefon' in favorites
print("6. 'telefon' mavjudmi?:", is_telefon)

# 7. 'naushnik' ni ro'yxatdan olib tashlang
favorites.remove('naushnik')
print("7. 'naushnik' o'chirildi:", favorites)

# 8. Oxirgi mahsulotni o'chiring
last_product = favorites.pop()
print("8. O'chirilgan mahsulot:", last_product)
print("   Qolgan ro'yxat:", favorites)

# 9. Ro'yxatni nusxalang va nusxaga 'televizor' qo'shing
favorites_copy = favorites.copy()
favorites_copy.append('televizor')
print("9. Nusxa ('televizor' qo'shilgan):", favorites_copy)

# 10. Ro'yxatni teskari tartibda tartiblang va chop eting
favorites.sort(reverse=True)
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat (teskari tartibda):", favorites)
print("    Nusxa ro'yxat:", favorites_copy)


# #11-masala
# Boshlang'ich ro'yxat
songs = ['Yomg\'ir', 'Sevgi', 'Hayot', 'Kuz']
print("Boshlang'ich ro'yxat:", songs)

# 1. 'Sevgi' dan oldin 'Bahor' qo'shing
index_sevgi = songs.index('Sevgi')
songs.insert(index_sevgi, 'Bahor')
print("1. 'Bahor' qo'shildi:", songs)

# 2. 'Kuz' ni ro'yxatdan olib tashlang
songs.remove('Kuz')
print("2. 'Kuz' o'chirildi:", songs)

# 3. Ro'yxatni alifbo tartibida tartiblang
songs.sort()
print("3. Alifbo tartibida:", songs)

# 4. 'Yomg'ir' ning indeksini toping
index_yomgir = songs.index('Yomg\'ir')
print("4. 'Yomg'ir' ning indeksi:", index_yomgir)

# 5. Ro'yxatda 'Hayot' mavjudligini tekshiring
is_hayot = 'Hayot' in songs
print("5. 'Hayot' mavjudmi?:", is_hayot)

# 6. Oxirgi qo'shiqni o'chiring
last_song = songs.pop()
print("6. O'chirilgan qo'shiq:", last_song)
print("   Qolgan ro'yxat:", songs)

# 7. Ro'yxatning uzunligini toping
length = len(songs)
print("7. Ro'yxat uzunligi:", length)

# 8. Ro'yxatni teskari tartibda tartiblang
songs.sort(reverse=True)
print("8. Teskari tartibda:", songs)

# 9. Ro'yxatni nusxalang va nusxaga 'Yoz' qo'shing
songs_copy = songs.copy()
songs_copy.append('Yoz')
print("9. Nusxa ('Yoz' qo'shilgan):", songs_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", songs)
print("    Nusxa ro'yxat:", songs_copy)


# #12-masala
# Boshlang'ich ro'yxat
books = ['Alximik', 'Shaytanat', '1984']
print("Boshlang'ich ro'yxat:", books)

# 1. Ro'yxatga 'O'tkan kunlar' va 'Sariq devni minib' qo'shing
books.extend(['O\'tkan kunlar', 'Sariq devni minib'])
print("1. Kitoblar qo'shildi:", books)

# 2. 'Shaytanat' ni ro'yxatdan olib tashlang
books.remove('Shaytanat')
print("2. 'Shaytanat' o'chirildi:", books)

# 3. Ro'yxatni alifbo tartibida tartiblang
books.sort()
print("3. Alifbo tartibida:", books)

# 4. '1984' ning indeksini toping
index_1984 = books.index('1984')
print("4. '1984' ning indeksi:", index_1984)

# 5. Ro'yxatda 'Alximik' mavjudligini tekshiring
is_alximik = 'Alximik' in books
print("5. 'Alximik' mavjudmi?:", is_alximik)

# 6. Oxirgi kitobni o'chiring
last_book = books.pop()
print("6. O'chirilgan kitob:", last_book)
print("   Qolgan ro'yxat:", books)

# 7. Ro'yxatning uzunligini toping
length = len(books)
print("7. Ro'yxat uzunligi:", length)

# 8. Ro'yxatni teskari tartibda tartiblang
books.sort(reverse=True)
print("8. Teskari tartibda:", books)

# 9. Ro'yxatni nusxalang va nusxaga 'Qirq yil' qo'shing
books_copy = books.copy()
books_copy.append('Qirq yil')
print("9. Nusxa ('Qirq yil' qo'shilgan):", books_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", books)
print("    Nusxa ro'yxat:", books_copy)


# #13-masala# Boshlang'ich ro'yxat
movies = ['Inception', 'Matrix', 'Interstellar']
print("Boshlang'ich ro'yxat:", movies)

# 1. Ro'yxatga 'Parasite' qo'shing
movies.append('Parasite')
print("1. 'Parasite' qo'shildi:", movies)

# 2. 'Matrix' ni ro'yxatdan olib tashlang
movies.remove('Matrix')
print("2. 'Matrix' o'chirildi:", movies)

# 3. Ro'yxatni alifbo tartibida tartiblang
movies.sort()
print("3. Alifbo tartibida:", movies)

# 4. 'Inception' ning indeksini toping
index_inception = movies.index('Inception')
print("4. 'Inception' ning indeksi:", index_inception)

# 5. Ro'yxatda 'Interstellar' mavjudligini tekshiring
is_interstellar = 'Interstellar' in movies
print("5. 'Interstellar' mavjudmi?:", is_interstellar)

# 6. Oxirgi filmni o'chiring
last_movie = movies.pop()
print("6. O'chirilgan film:", last_movie)
print("   Qolgan ro'yxat:", movies)

# 7. Ro'yxatning uzunligini toping
length = len(movies)
print("7. Ro'yxat uzunligi:", length)

# 8. Ro'yxatni teskari tartibda tartiblang
movies.sort(reverse=True)
print("8. Teskari tartibda:", movies)

# 9. Ro'yxatni nusxalang va nusxaga 'Joker' qo'shing
movies_copy = movies.copy()
movies_copy.append('Joker')
print("9. Nusxa ('Joker' qo'shilgan):", movies_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", movies)
print("    Nusxa ro'yxat:", movies_copy)


# #14-masala
# Boshlang'ich ro'yxat
emails = ['job_offer', 'spam', 'friend', 'news']
print("Boshlang'ich ro'yxat:", emails)

# 1. Ro'yxatga 'family' qo'shing
emails.append('family')
print("1. 'family' qo'shildi:", emails)

# 2. 'spam' ni ro'yxatdan olib tashlang
emails.remove('spam')
print("2. 'spam' o'chirildi:", emails)

# 3. Ro'yxatni alifbo tartibida tartiblang
emails.sort()
print("3. Alifbo tartibida:", emails)

# 4. 'friend' ning indeksini toping
index_friend = emails.index('friend')
print("4. 'friend' ning indeksi:", index_friend)

# 5. Ro'yxatda 'job_offer' mavjudligini tekshiring
is_job_offer = 'job_offer' in emails
print("5. 'job_offer' mavjudmi?:", is_job_offer)

# 6. Oxirgi xabarni o'chiring
last_email = emails.pop()
print("6. O'chirilgan xabar:", last_email)
print("   Qolgan ro'yxat:", emails)

# 7. Ro'yxatning uzunligini toping
length = len(emails)
print("7. Ro'yxat uzunligi:", length)

# 8. Ro'yxatni teskari tartibda tartiblang
emails.sort(reverse=True)
print("8. Teskari tartibda:", emails)

# 9. Ro'yxatni nusxalang va nusxaga 'urgent' qo'shing
emails_copy = emails.copy()
emails_copy.append('urgent')
print("9. Nusxa ('urgent' qo'shilgan):", emails_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", emails)
print("    Nusxa ro'yxat:", emails_copy)


# #15-masala
# Boshlang'ich ro'yxat
friends = ['Ali', 'Zara', 'Bobur', 'Nodir']
print("Boshlang'ich ro'yxat:", friends)

# 1. Ro'yxatga 'Jamol' qo'shing
friends.append('Jamol')
print("1. 'Jamol' qo'shildi:", friends)

# 2. 'Nodir' ni ro'yxatdan olib tashlang
friends.remove('Nodir')
print("2. 'Nodir' o'chirildi:", friends)

# 3. Ro'yxatni alifbo tartibida tartiblang
friends.sort()
print("3. Alifbo tartibida:", friends)

# 4. 'Zara' ning indeksini toping
index_zara = friends.index('Zara')
print("4. 'Zara' ning indeksi:", index_zara)

# 5. Ro'yxatda 'Ali' mavjudligini tekshiring
is_ali = 'Ali' in friends
print("5. 'Ali' mavjudmi?:", is_ali)

# 6. Oxirgi do'stni o'chiring
last_friend = friends.pop()
print("6. O'chirilgan do'st:", last_friend)
print("   Qolgan ro'yxat:", friends)

# 7. Ro'yxatning uzunligini toping
length = len(friends)
print("7. Ro'yxat uzunligi:", length)

# 8. Ro'yxatni teskari tartibda tartiblang
friends.sort(reverse=True)
print("8. Teskari tartibda:", friends)

# 9. Ro'yxatni nusxalang va nusxaga 'Sardor' qo'shing
friends_copy = friends.copy()
friends_copy.append('Sardor')
print("9. Nusxa ('Sardor' qo'shilgan):", friends_copy)

# 10. Asl ro'yxat va nusxani chop eting
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", friends)
print("    Nusxa ro'yxat:", friends_copy)


# #16-masala
# Boshlang'ich ro'yxat
animals = ['sher', 'yo\'lbars', 'ayiq', 'sher', 'quyon']
print("Boshlang'ich ro'yxat:", animals)

# 1. Ro'yxatda 'sher' nechta borligini aniqlang
count_sher = animals.count('sher')
print("1. 'sher' soni:", count_sher)

# 2. 'ayiq' ni ro'yxatdan olib tashlang
animals.remove('ayiq')
print("2. 'ayiq' o'chirildi:", animals)

# 3. Asl ro'yxatga 'kenguru' ni oxiriga qo'shing
animals.append('kenguru')
print("3. 'kenguru' qo'shildi:", animals)

# 4. Ro'yxatni alifbo tartibida tartiblang
animals.sort()
print("4. Alifbo tartibida:", animals)

# 5. 'yo'lbars' ning indeksini toping
index_yolbars = animals.index('yo\'lbars')
print("5. 'yo'lbars' ning indeksi:", index_yolbars)

# 6. Ro'yxatda 'quyon' mavjudligini tekshiring
is_quyon = 'quyon' in animals
print("6. 'quyon' mavjudmi?:", is_quyon)

# 7. Oxirgi hayvonni o'chiring
last_animal = animals.pop()
print("7. O'chirilgan hayvon:", last_animal)
print("   Qolgan ro'yxat:", animals)

# 8. Ro'yxatning uzunligini toping
length = len(animals)
print("8. Ro'yxat uzunligi:", length)

# 9. Ro'yxatni nusxalang va nusxaga 'tuya' qo'shing
animals_copy = animals.copy()
animals_copy.append('tuya')
print("9. Nusxa ('tuya' qo'shilgan):", animals_copy)

# 10. Asl ro'yxat va nusxani chop eting va farqlarini tahlil qiling
print("\n10. Yakuniy natijalar va tahlil:")
print("    Asl ro'yxat:", animals)
print("    Nusxa ro'yxat:", animals_copy)
print("    Farq: Nusxada 'tuya' bor, aslida yo'q")


# #17-masala
# Boshlang'ich ro'yxat
champions = ['Khamzat Chimaev', 'Khabib Nurmagomedov', 'Conor McGregor', 
             'Mike Tyson', 'Wladimir Klichko', 'Eliud']
print("Boshlang'ich ro'yxat:", champions)

# 1. Ro'yxatda 'Mike Tyson' nechta borligini aniqlang
count_tyson = champions.count('Mike Tyson')
print("1. 'Mike Tyson' soni:", count_tyson)

# 2. Oxirgi ishtirokchini o'chiring
last_champion = champions.pop()
print("2. O'chirilgan ishtirokchi:", last_champion)
print("   Qolgan ro'yxat:", champions)

# 3. Ro'yxatga 'Bahodir Jalolov' va 'Hasanboy Do'smatov' ni qo'shing
champions.extend(['Bahodir Jalolov', 'Hasanboy Do\'smatov'])
print("3. Yangi ishtirokchilar qo'shildi:", champions)

# 4. Ro'yxatni alifbo tartibida tartiblang
champions.sort()
print("4. Alifbo tartibida:", champions)

# 5. Tartiblangan ro'yxatda 'Mike Tyson' ning yangi indeksini toping
index_tyson = champions.index('Mike Tyson')
print("5. 'Mike Tyson' ning yangi indeksi:", index_tyson)

# 6. Ro'yxatda 'Khabib Nurmagomedov' mavjudligini tekshiring
is_khabib = 'Khabib Nurmagomedov' in champions
print("6. 'Khabib Nurmagomedov' mavjudmi?:", is_khabib)

# 7. 'Conor McGregor' ni ro'yxatdan olib tashlang
champions.remove('Conor McGregor')
print("7. 'Conor McGregor' o'chirildi:", champions)

# 8. Ro'yxatning uzunligini toping
length = len(champions)
print("8. Ro'yxat uzunligi:", length)

# 9. Ro'yxatni nusxalang va nusxaga 'Shaxram G'iyasov' ni qo'shing
champions_copy = champions.copy()
champions_copy.append('Shaxram G\'iyasov')
print("9. Nusxa ('Shaxram G'iyasov' qo'shilgan):", champions_copy)

# 10. Asl ro'yxat va nusxani chop eting va o'zgarishlarni taqqoslang
print("\n10. Yakuniy natijalar va taqqoslash:")
print("    Asl ro'yxat:", champions)
print("    Nusxa ro'yxat:", champions_copy)
print("    O'zgarish: Nusxada 'Shaxram G'iyasov' qo'shilgan")


# #18-masala
# Boshlang'ich ro'yxat
cart = ['non', 'suyut', 'tuxum', "go'sht"]
print("Boshlang'ich ro'yxat:", cart)

# 1. 'tuxum' elementining indeksini toping
index_tuxum = cart.index('tuxum')
print("1. 'tuxum' ning indeksi:", index_tuxum)

# 2. 'suyut' ni ro'yxatdan olib tashlang
cart.remove('suyut')
print("2. 'suyut' o'chirildi:", cart)

# 3. Ro'yxatga 'sari yog'' va 'murabbo' qo'shing
cart.extend(['sari yog\'', 'murabbo'])
print("3. Yangi mahsulotlar qo'shildi:", cart)

# 4. Ro'yxatni alifbo tartibida tartiblang
cart.sort()
print("4. Alifbo tartibida:", cart)

# 5. Ro'yxatni nusxalang va nusxaga 'shakar' qo'shing
cart_copy = cart.copy()
cart_copy.append('shakar')
print("5. Nusxa ('shakar' qo'shilgan):", cart_copy)

# 6. Asl ro'yxatni bo'shating
cart.clear()
print("6. Asl ro'yxat bo'shatildi:", cart)

# 7. Bo'shatilgan ro'yxatda 'non' mavjudligini tekshiring
is_non = 'non' in cart
print("7. 'non' mavjudmi? (False bo'lishi kerak):", is_non)

# 8. Bo'shatilgan ro'yxatning uzunligini toping
length = len(cart)
print("8. Bo'sh ro'yxat uzunligi (0 bo'lishi kerak):", length)

# 9. Nusxa ro'yxatdan oxirgi mahsulotni o'chiring
last_product = cart_copy.pop()
print("9. Nusxadan o'chirilgan mahsulot:", last_product)
print("   Nusxada qolgan:", cart_copy)

# 10. Asl ro'yxat (bo'sh) va nusxani chop eting va natijalarni tahlil qiling
print("\n10. Yakuniy natijalar va tahlil:")
print("    Asl ro'yxat (bo'sh):", cart)
print("    Nusxa ro'yxat:", cart_copy)
print("    Tahlil: clear() metodi asl ro'yxatni butunlay bo'shatdi,")
print("           lekin nusxa o'z ma'lumotlarini saqladi.")


# #19-masala# Boshlang'ich ro'yxat
courses = ['Python', 'Java', 'Data Science', 'Python']
print("Boshlang'ich ro'yxat:", courses)

# 1. Ro'yxatda 'Python' nechta borligini aniqlang
count_python = courses.count('Python')
print("1. 'Python' soni (2 bo'lishi kerak):", count_python)

# 2. 'Java' ni ro'yxatdan olib tashlang
courses.remove('Java')
print("2. 'Java' o'chirildi:", courses)

# 3. Ro'yxatga 'AI' va 'Web Development' qo'shing
courses.extend(['AI', 'Web Development'])
print("3. Yangi kurslar qo'shildi:", courses)

# 4. Ro'yxatni alifbo tartibida tartiblang
courses.sort()
print("4. Alifbo tartibida (Python lar yonma-yon):", courses)

# 5. Tartiblangan ro'yxatda 'Data Science' ning indeksini toping
index_ds = courses.index('Data Science')
print("5. 'Data Science' ning indeksi:", index_ds)

# 6. Ro'yxatda 'AI' mavjudligini tekshiring
is_ai = 'AI' in courses
print("6. 'AI' mavjudmi?:", is_ai)

# 7. Oxirgi kursni o'chiring
last_course = courses.pop()
print("7. O'chirilgan kurs:", last_course)
print("   Qolgan ro'yxat:", courses)

# 8. Birinchi 'Python' ni ro'yxatdan olib tashlang
courses.remove('Python')
print("8. Birinchi 'Python' o'chirildi:", courses)

# 9. Ro'yxatning uzunligini toping
length = len(courses)
print("9. Ro'yxat uzunligi:", length)

# 10. Ro'yxatni nusxalang va nusxaga 'Blockchain' qo'shing
courses_copy = courses.copy()
courses_copy.append('Blockchain')
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat:", courses)
print("    Nusxa ro'yxat:", courses_copy)


# #20-masala
# Boshlang'ich ro'yxat
cars = ['Chevrolet', 'Hyundai', 'Kia', 'Toyota']
print("Boshlang'ich ro'yxat:", cars)

# 1. Ro'yxat boshiga 'BMW' qo'shing
cars.insert(0, 'BMW')
print("1. 'BMW' boshiga qo'shildi:", cars)

# 2. 'Kia' ni ro'yxatdan olib tashlang
cars.remove('Kia')
print("2. 'Kia' o'chirildi:", cars)

# 3. Ro'yxatni nusxalang (o'zgarishlardan oldin)
cars_copy = cars.copy()
print("3. Nusxa olindi (o'zgarishlardan oldin):", cars_copy)

# 4. Asl ro'yxatni alifbo tartibida tartiblang
cars.sort()
print("4. Asl ro'yxat alifbo tartibida:", cars)

# 5. Tartiblangan asl ro'yxatda 'Toyota' ning indeksini toping
index_toyota = cars.index('Toyota')
print("5. 'Toyota' ning indeksi:", index_toyota)

# 6. Asl ro'yxatda 'Hyundai' mavjudligini tekshiring
is_hyundai = 'Hyundai' in cars
print("6. 'Hyundai' mavjudmi?:", is_hyundai)

# 7. Asl ro'yxatdan oxirgi mashinani o'chiring
last_car = cars.pop()
print("7. O'chirilgan mashina:", last_car)
print("   Qolgan ro'yxat:", cars)

# 8. Asl ro'yxatning uzunligini toping
length = len(cars)
print("8. Asl ro'yxat uzunligi:", length)

# 9. Asl ro'yxatni teskari tartibda tartiblang
cars.sort(reverse=True)
print("9. Asl ro'yxat teskari tartibda:", cars)

# 10. Asl ro'yxatni bo'shating, nusxaga 'Mercedes' qo'shing
cars.clear()
cars_copy.append('Mercedes')
print("\n10. Yakuniy natijalar:")
print("    Asl ro'yxat (bo'sh):", cars)
print("    Nusxa ro'yxat:", cars_copy)
print("    Natija: Asl ro'yxat bo'sh, nusxa o'zgarishdan oldingi")
print("            holatni saqladi va 'Mercedes' qo'shildi.")




## TUPLE MASALALARI (1-10)
# #1-masala
# Boshlang'ich tuple
days = ('Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma')
print("Boshlang'ich tuple:", days)

# 1. Tuple uzunligini toping
length = len(days)
print("1. Tuple uzunligi:", length)

# 2. 'Juma' elementi mavjudligini tekshiring
is_juma = 'Juma' in days
print("2. 'Juma' mavjudmi?:", is_juma)

# 3. 'Chorshanba' ning indeksini toping
index_chorshanba = days.index('Chorshanba')
print("3. 'Chorshanba' ning indeksi:", index_chorshanba)

# 4. Tuple dan 2-chi elementni oling
second_day = days[1]
print("4. 2-chi element (indeks 1):", second_day)

# 5. Faqat oxirgi 2 ta kunni kesib oling
last_two = days[-2:]
print("5. Oxirgi 2 ta kun:", last_two)

# 6. Tuple ni ro'yxatga aylantiring
days_list = list(days)
print("6. Ro'yxatga aylantirildi:", days_list)

# 7. Ro'yxatga 'Shanba' va 'Yakshanba' qo'shing
days_list.append('Shanba')
days_list.append('Yakshanba')
print("7. Dam olish kunlari qo'shildi:", days_list)

# 8. Uni qayta tuple'ga aylantiring
days_full = tuple(days_list)
print("8. Qayta tuple'ga aylandi:", days_full)

# 9. Yakuniy tuple uzunligini toping
final_length = len(days_full)
print("9. Yakuniy tuple uzunligi:", final_length)

# 10. Yakuniy tuple'ni chop eting
print("10. Yakuniy tuple:", days_full)


# #2-masala
# Boshlang'ich tuple
colors = ('qizil', 'yashil', 'ko\'k', 'sariq')
print("Boshlang'ich tuple:", colors)

# 1. 'yashil' mavjudligini tekshiring
is_yashil = 'yashil' in colors
print("1. 'yashil' mavjudmi?:", is_yashil)

# 2. 'qora' mavjud emasligini tekshiring
is_not_qora = 'qora' not in colors
print("2. 'qora' mavjud emasmi?:", is_not_qora)

# 3. Tuple uzunligini toping
length = len(colors)
print("3. Tuple uzunligi:", length)

# 4. 'ko'k' ning indeksini toping
index_kok = colors.index('ko\'k')
print("4. 'ko'k' ning indeksi:", index_kok)

# 5. Tuple ni ro'yxatga aylantirib 'pushti' ni qo'shing
colors_list = list(colors)
colors_list.append('pushti')
print("5. 'pushti' qo'shildi:", colors_list)

# 6. Ro'yxatni qayta tuple'ga aylantiring
colors = tuple(colors_list)
print("6. Qayta tuple:", colors)

# 7. Tuple ichidagi 2-3 elementlarni kesib oling
colors_slice = colors[1:3]
print("7. 2-3 elementlar:", colors_slice)

# 8. Tuple'ni 2 marta takrorlang
colors_doubled = colors * 2
print("8. 2 marta takrorlandi:", colors_doubled)

# 9. Yangi tuple uzunligini toping
new_length = len(colors_doubled)
print("9. Yangi tuple uzunligi:", new_length)

# 10. Natijani chop eting
print("10. Yakuniy natija:", colors_doubled)


# #3-masala
# Boshlang'ich tuple
cities = ('Toshkent', 'Buxoro', 'Xiva', 'Samarqand')
print("Boshlang'ich tuple:", cities)

# 1. 'Buxoro' ning indeksini toping
index_buxoro = cities.index('Buxoro')
print("1. 'Buxoro' ning indeksi:", index_buxoro)

# 2. Tuple uzunligini toping
length = len(cities)
print("2. Tuple uzunligi:", length)

# 3. 'Navoiy' tuple'da mavjud emasligini tekshiring
is_not_navoiy = 'Navoiy' not in cities
print("3. 'Navoiy' mavjud emasmi?:", is_not_navoiy)

# 4. Faqat 1-2-3 elementlarni kesib oling
cities_slice = cities[1:4]
print("4. 1-2-3 elementlar:", cities_slice)

# 5. Tuple ni ro'yxatga o'tkazib, 'Navoiy' ni qo'shing
cities_list = list(cities)
cities_list.append('Navoiy')
print("5. 'Navoiy' qo'shildi:", cities_list)

# 6. Ro'yxatni qayta tuple'ga aylantiring
cities = tuple(cities_list)
print("6. Qayta tuple:", cities)

# 7. Har bir elementni for orqali chop eting
print("7. Har bir shahar:")
for city in cities:
    print("   -", city)

# 8. Tuple'dan oxirgi elementni oling
last_city = cities[-1]
print("8. Oxirgi shahar:", last_city)

# 9. Tuple ni 2 marta takrorlang
cities_doubled = cities * 2
print("9. 2 marta takrorlandi:", cities_doubled)

# 10. Yakuniy natijani chop eting
print("10. Yakuniy natija:", cities_doubled)


# #4-masala
# Boshlang'ich tuple
scores = (78, 92, 65, 88, 100)
print("Boshlang'ich tuple:", scores)

# 1. Eng katta ballni toping
max_score = max(scores)
print("1. Eng katta ball:", max_score)

# 2. Eng kichik ballni toping
min_score = min(scores)
print("2. Eng kichik ball:", min_score)

# 3. Ballar o'rtacha qiymatini toping
average = sum(scores) / len(scores)
print("3. O'rtacha ball:", average)

# 4. 92 mavjudligini tekshiring
is_92 = 92 in scores
print("4. 92 mavjudmi?:", is_92)

# 5. Tuple uzunligini toping
length = len(scores)
print("5. Tuple uzunligi:", length)

# 6. Tuple'ni ro'yxatga o'tkazib, 85 ball qo'shing
scores_list = list(scores)
scores_list.append(85)
print("6. 85 ball qo'shildi:", scores_list)

# 7. Ro'yxatni qayta tuple'ga aylantiring
scores = tuple(scores_list)
print("7. Qayta tuple:", scores)

# 8. 80 dan katta balllarni ajrating
high_scores = tuple([score for score in scores if score > 80])
print("8. 80 dan katta ballar:", high_scores)

# 9. Tuple'dagi 3-chi elementni oling (indeks 2)
third_element = scores[2]
print("9. 3-chi element:", third_element)

# 10. Yakuniy tuple'ni chop eting
print("10. Yakuniy tuple:", scores)


# #5-masala
# Boshlang'ich tuple
movies = ('Titanic', 'Avatar', 'Inception', 'Joker')
print("Boshlang'ich tuple:", movies)

# 1. 'Avatar' mavjudligini tekshiring
is_avatar = 'Avatar' in movies
print("1. 'Avatar' mavjudmi?:", is_avatar)

# 2. 'Matrix' yo'qligini tekshiring
is_not_matrix = 'Matrix' not in movies
print("2. 'Matrix' yo'qmi?:", is_not_matrix)

# 3. Tuple uzunligini toping
length = len(movies)
print("3. Tuple uzunligi:", length)

# 4. 'Joker' ning indeksini toping
index_joker = movies.index('Joker')
print("4. 'Joker' ning indeksi:", index_joker)

# 5. Tuple ni ro'yxatga aylantirib 'Matrix' ni qo'shing
movies_list = list(movies)
movies_list.append('Matrix')
print("5. 'Matrix' qo'shildi:", movies_list)

# 6. Ro'yxatni qayta tuple'ga aylantiring
movies = tuple(movies_list)
print("6. Qayta tuple:", movies)

# 7. 2-dan 4-elementgacha bo'lgan qismini oling
movies_slice = movies[1:4]
print("7. 2-dan 4-elementgacha:", movies_slice)

# 8. Tuple'ni 2 marta takrorlang
movies_doubled = movies * 2
print("8. 2 marta takrorlandi:", movies_doubled)

# 9. Tuple ichidagi barcha elementlarni for bilan chiqarib chiqing
print("9. Barcha filmlar:")
for movie in movies:
    print("   -", movie)

# 10. Yakuniy natijani chop eting
print("10. Yakuniy natija:", movies_doubled)


# # 6-masala
# Boshlang'ich tuple
menu = ('osh', 'lag\'mon', 'shashlik', 'somsa')
print("Boshlang'ich tuple:", menu)

# 1. 'somsa' mavjudligini tekshiring
is_somsa = 'somsa' in menu
print("1. 'somsa' mavjudmi?:", is_somsa)

# 2. 'manti' yo'qligini tekshiring
is_not_manti = 'manti' not in menu
print("2. 'manti' yo'qmi?:", is_not_manti)

# 3. Tuple uzunligini toping
length = len(menu)
print("3. Tuple uzunligi:", length)

# 4. 'lag'mon' ning indeksini toping
index_lagmon = menu.index('lag\'mon')
print("4. 'lag'mon' ning indeksi:", index_lagmon)

# 5. Tuple ni ro'yxatga aylantirib 'manti' ni qo'shing
menu_list = list(menu)
menu_list.append('manti')
print("5. 'manti' qo'shildi:", menu_list)

# 6. 'osh' ni ro'yxatdan o'chirib tashlang
menu_list.remove('osh')
print("6. 'osh' o'chirildi:", menu_list)

# 7. Ro'yxatni qayta tuple'ga aylantiring
menu = tuple(menu_list)
print("7. Qayta tuple:", menu)

# 8. Tuple'ni 2 marta takrorlang
menu_doubled = menu * 2
print("8. 2 marta takrorlandi:", menu_doubled)

# 9. 1-dan 3-elementgacha bo'lgan qismini oling
menu_slice = menu[1:4]
print("9. 1-dan 3-elementgacha:", menu_slice)

# 10. Yakuniy natijani chop eting
print("10. Yakuniy natija:", menu_doubled)


# #7-masala
# Boshlang'ich tuple
genres = ('pop', 'rap', 'rock', 'jazz', 'classic')
print("Boshlang'ich tuple:", genres)

# 1. 'rock' indeksini toping
index_rock = genres.index('rock')
print("1. 'rock' ning indeksi:", index_rock)

# 2. 'blues' mavjud emasligini tekshiring
is_not_blues = 'blues' not in genres
print("2. 'blues' mavjud emasmi?:", is_not_blues)

# 3. Tuple uzunligini toping
length = len(genres)
print("3. Tuple uzunligi:", length)

# 4. Tuple ni ro'yxatga aylantiring
genres_list = list(genres)
print("4. Ro'yxatga aylantirildi:", genres_list)

# 5. 'blues' va 'electro' janrlarini qo'shing
genres_list.append('blues')
genres_list.append('electro')
print("5. 'blues' va 'electro' qo'shildi:", genres_list)

# 6. Ro'yxatni qayta tuple'ga aylantiring
genres = tuple(genres_list)
print("6. Qayta tuple:", genres)

# 7. Tuple'ni alifbo tartibida chiqaring
genres_sorted = tuple(sorted(genres))
print("7. Alifbo tartibida:", genres_sorted)

# 8. 3-chi elementni oling (indeks 2)
third_element = genres[2]
print("8. 3-chi element:", third_element)

# 9. Tuple'ni 3 marta takrorlang
genres_tripled = genres * 3
print("9. 3 marta takrorlandi:", genres_tripled)

# 10. Natijani chop eting
print("10. Yakuniy natija:", genres_tripled)


# #8-masala
# Boshlang'ich tuple
phones = ('iPhone', 'Samsung', 'Nokia', 'Xiaomi', 'Huawei')
print("Boshlang'ich tuple:", phones)

# 1. 'Samsung' indeksini toping
index_samsung = phones.index('Samsung')
print("1. 'Samsung' ning indeksi:", index_samsung)

# 2. 'LG' mavjudligini tekshiring
is_lg = 'LG' in phones
print("2. 'LG' mavjudmi?:", is_lg)

# 3. Tuple uzunligini toping
length = len(phones)
print("3. Tuple uzunligi:", length)

# 4. Tuple ni ro'yxatga o'tkazib 'Realme' qo'shing
phones_list = list(phones)
phones_list.append('Realme')
print("4. 'Realme' qo'shildi:", phones_list)

# 5. 'Nokia' ni olib tashlang
phones_list.remove('Nokia')
print("5. 'Nokia' o'chirildi:", phones_list)

# 6. Ro'yxatni qayta tuple'ga aylantiring
phones = tuple(phones_list)
print("6. Qayta tuple:", phones)

# 7. Tuple'dan 2-dan oxirigacha kesib oling
phones_slice = phones[2:]
print("7. 2-dan oxirigacha:", phones_slice)

# 8. Tuple'ni 2 marta takrorlang
phones_doubled = phones * 2
print("8. 2 marta takrorlandi:", phones_doubled)

# 9. Har bir elementni for bilan chiqarib chiqing
print("9. Barcha telefonlar:")
for phone in phones:
    print("   -", phone)

# 10. Yakuniy tuple'ni chop eting
print("10. Yakuniy tuple:", phones)


# #9-masala
# Boshlang'ich tuple
books = ('1984', 'Shaytanat', 'Alkimyogar', 'O\'tkan kunlar')
print("Boshlang'ich tuple:", books)

# 1. '1984' mavjudligini tekshiring
is_1984 = '1984' in books
print("1. '1984' mavjudmi?:", is_1984)

# 2. 'Sariq devni minib' yo'qligini tekshiring
is_not_sariq = 'Sariq devni minib' not in books
print("2. 'Sariq devni minib' yo'qmi?:", is_not_sariq)

# 3. Tuple uzunligini toping
length = len(books)
print("3. Tuple uzunligi:", length)

# 4. 'Shaytanat' indeksini toping
index_shaytanat = books.index('Shaytanat')
print("4. 'Shaytanat' ning indeksi:", index_shaytanat)

# 5. Tuple ni ro'yxatga aylantiring
books_list = list(books)
print("5. Ro'yxatga aylantirildi:", books_list)

# 6. 'Sariq devni minib' qo'shing
books_list.append('Sariq devni minib')
print("6. 'Sariq devni minib' qo'shildi:", books_list)

# 7. Ro'yxatni qayta tuple'ga aylantiring
books = tuple(books_list)
print("7. Qayta tuple:", books)

# 8. Tuple'dan faqat oxirgi 2 elementni oling
last_two = books[-2:]
print("8. Oxirgi 2 element:", last_two)

# 9. Tuple'ni 3 marta takrorlang
books_tripled = books * 3
print("9. 3 marta takrorlandi:", books_tripled)

# 10. Yakuniy natijani chop eting
print("10. Yakuniy natija:", books_tripled)


# #10-masala
# Boshlang'ich tuple
cars = ('BMW', 'Chevrolet', 'Hyundai', 'Toyota')
print("Boshlang'ich tuple:", cars)

# 1. 'BMW' indeksini toping
index_bmw = cars.index('BMW')
print("1. 'BMW' ning indeksi:", index_bmw)

# 2. 'Kia' mavjud emasligini tekshiring
is_not_kia = 'Kia' not in cars
print("2. 'Kia' mavjud emasmi?:", is_not_kia)

# 3. Tuple uzunligini toping
length = len(cars)
print("3. Tuple uzunligi:", length)

# 4. Tuple ni ro'yxatga aylantirib 'Kia' qo'shing
cars_list = list(cars)
cars_list.append('Kia')
print("4. 'Kia' qo'shildi:", cars_list)

# 5. 'Hyundai' ni olib tashlang
cars_list.remove('Hyundai')
print("5. 'Hyundai' o'chirildi:", cars_list)

# 6. Ro'yxatni qayta tuple'ga aylantiring
cars = tuple(cars_list)
print("6. Qayta tuple:", cars)

# 7. 2-elementdan boshlab kesing (indeks 1 dan)
cars_slice = cars[1:]
print("7. 2-elementdan boshlab:", cars_slice)

# 8. Tuple'ni 2 marta takrorlang
cars_doubled = cars * 2
print("8. 2 marta takrorlandi:", cars_doubled)

# 9. Tuple ni sorted() bilan tartiblang
cars_sorted = tuple(sorted(cars))
print("9. Alifbo tartibida:", cars_sorted)

# 10. Yakuniy tuple'ni chop eting
print("10. Yakuniy tuple:", cars_sorted)