#KARŞILAŞTIRMA OPERATÖRLERİ
"""
<  : küçüktür
>  : büyüktür
<= : küçük eşit
>= : büyük eşit
== : eşittir
!= : eşit değildir
"""
cinsiyet=input("Bir harf giriniz:")
if cinsiyet=="e" or cinsiyet=="E": #or: 2 şarttan biri doğru ise çalışır.
    print("Cinsiyet olarak erkek girdiniz.")
    print("if içerisinden selamlar")
elif cinsiyet=="k" or cinsiyet=="K": #2. veya daha sonraki şartları eklemek için elif kullanılır.
    print("Cinsiyet olarak kadın girdiniz")
    print("Şuanda elif içinden mesaj veriyorum")
else: #şartların dışında herhangi bir şey girilirse çalışır.
    print("Ben sana e ya da k gir demedim mi?")
print("Şuanda if dışındasın, if in bitti !")

