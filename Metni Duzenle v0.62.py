import pyperclip

def duzenle():
	pano_icerigi = pyperclip.paste()
	# # print("PANO İÇERİĞİ:\n", pano_icerigi)
	
	satirlar = pano_icerigi.split("\n")
	# # print("SATIRLAR:\n", satirlar)
	
	metin = ""
	
	for s in satirlar:
		if s[-1] == "." or s[-1] == ";":
			metin += s + "\n\n"
		
		else:
			metin += s + " "
	
	# # print(metin)
	
	del satirlar			# "satirlar" listesini sil

	# # Düzenlenmiş Metni Panoya kopyalama kodu;
	pyperclip.copy(metin)
	print("Düzenlenmiş metin panoya kopyalandı.")
		
duzenle()

