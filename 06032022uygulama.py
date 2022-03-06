#kullanıcıdan isim, soyisim, telefon numarası alarak bir listeye atayınız.
bilgiler=[] #boş liste tanımlar.
print("Lütfen aşağıdaki bilgileri doldurunuz.")
isim=input("isminiz:")
soyisim=input("soyadınız:")
telefonnumarası=input("Telefon Numaranız:")
bilgiler.append(isim)
bilgiler.append(soyisim)
bilgiler.append(telefonnumarası)
print(bilgiler)
print("Adı:",bilgiler[0])
print("Soyadı:")