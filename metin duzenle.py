txt_dosya = "metin"	# satırlarını birleştirmek istediğimiz ".txt" uzantılı dosya adını belirttik.

with open(txt_dosya + ".txt", "r", encoding="utf-8") as dosya: 
    satirlar = dosya.readlines()    # liste veri tipi
    # print(satirlar)

############# 1
    liste_gecici_satirlar = []    # işlemler arası (ENTER'siz düzenleme için) kullanılan geçici liste

    for satir in satirlar:
        liste_gecici_satirlar.append(satir[:-1])
    # print("ENTER'siz liste_gecici_satirlar:\n", liste_gecici_satirlar)
############# 1    


############# 2.2
    icerik = ""  # alt satıra taşan kelimelerin birleştirilmiş halde toplandığı içerik

    for i in range(len(liste_gecici_satirlar)):           # satır sonunda "-" ifadesi olan satır ile bir alt satır birleştiriliyor.
        if not liste_gecici_satirlar[i].endswith("-"):
            icerik += (liste_gecici_satirlar[i] + " ")
        else:
            icerik += liste_gecici_satirlar[i][:-1]
    
    icerik = icerik.replace(". ", ". \n") # her cümle ayrı bir satıra bölünsün.
    # print("KELİMELER BİRLEŞTİRİLDİ TİRESİZ:\n", icerik)
############# 2.2


############# 4
    with open(txt_dosya + "_duzenlendi.txt", "w", encoding="utf-8") as cikti:
        cikti.write(icerik)
############# 4        
