import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit() 
def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute('Insert into kitaplık Values(?,?,?,?)',(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()    
#Verileri göstermek
def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print('Kitaplık tablosunun bilgileri...')
    for i in liste:
        print(i)
#Sadece İsim ve Yazar özelliği almak.
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Sadece isim ve yazar")
    for i in liste:
        print(i)
#İstenilen datayı tek olarak inputla sorgulama
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)
#İstenilen verileri Güncelleme
def verileriguncelle(eskiyayınevi,yeniyayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? Where Yayınevi = ?",(yeniyayınevi,eskiyayınevi))
    con.commit()
#Verileri Silmek
def verilerisil(yazar):
    cursor.execute("Delete From kitaplık where Yazar = ?",(yazar,))
    con.commit()
con.close()


