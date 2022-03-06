"""
kullanıcı yılsonu ortalaması girsin.Ortalama 85 üstü ise taktir, 70 üstü teşekkür,
bunların dışında ise hiçbir belge alamadınız desin..
"""
ortalama=int(input("Yıl sonu ortalamanızı giriniz:"))
if ortalama>=85:
    print("taktir belgesi aldınız.")
elif ortalama>=70:
    print("Teşekkür belgesi aldınız")
else:
    print("hiçbir şey alamadınız.")