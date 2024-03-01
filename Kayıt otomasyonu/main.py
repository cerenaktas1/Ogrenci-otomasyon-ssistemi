import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['db_ogrenciler']
table = db['ogrenci']

def ogr_ekle():
    no = int(input("öğrenci no: "))
    ad = input("öğrenci adı: ")
    soyad = input("öğrenci soyadı: ")

    table.insert_one({"no": no, "ad": ad, "soyad": soyad})
    for i in table.find({"no": no}):
        print(
            """ --- Öğrenci bilgileri eklendi ---
                   numara  : {}
                   ad      : {}
                   soyad   : {}""".format(i['no'], i['ad'], i['soyad']))

def ogr_sil():
    no = int(input("silmek istediğiniz öğrencinin numarasını giriniz: "))

    for i in table.find({"no": no}):
        print(
            """ --- Öğrenci bilgileri silindi ---
               numara  : {}
               ad      : {}
               soyad   : {}""".format(i['no'], i['ad'], i['soyad']))

    table.delete_one({"no": no})

def ogr_ara():
    no = int(input("aramak istediğiniz öğrencinin numarasını giriniz: "))

    for i in table.find({"no": no}):
        print(
            """ --- Öğrenci bilgileri bulundu ---
                   numara  : {}
                   ad      : {}
                   soyad   : {}""".format(i['no'], i['ad'], i['soyad']))

def ogr_lis():
    sonuc = table.find()
    for (a, i) in enumerate(sonuc):
        print(
            """
                   --- {} ---
                   numara  : {}
                   ad      : {}
                   soyad   : {} """.format(a, i['no'], i['ad'], i['soyad']))

def main():
    print(
        """
           Öğrenci Kayıt Otomasyonu
       
           1 - Öğrenci ekle
           2 - Öğrenci ara
           3 - Öğrenci sil
           4 - Öğrenci listele
           5 - Çıkış
        """)

    while True:
        secim = input("Yapmak istediğiniz işlemi seçin: ")

        if secim == '1':
            ogr_ekle()
        elif secim == '2':
            ogr_ara()
        elif secim == '3':
            ogr_sil()
        elif secim == '4':
            ogr_lis()
        elif secim == '5':
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == '__main__':
    main()
