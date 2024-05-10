import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import pyperclip

style = Style(theme='minty')	# superhero, minty, lumen, sandstone, cerculean, simplex, morph, united, darkly, 

pencere = style.master
pencere.geometry("850x425+400+200")
pencere.title(".:: Metni Düzenle (v 0.4) - Mustafa Halil ::. ")

def duzenle():
	pano_icerigi = pencere.clipboard_get().split(" ")
	# # print("PANO İÇERİĞİ:", pano_icerigi)
	
	
	gecici1 = []
	gecici2 = []
	gecici_liste_2 = []
	nihai = ""
	
	if pano_icerigi != "":
		
		for kelime in pano_icerigi:
			
			if kelime != "":
				gecici1.append(kelime)
		
		# # print("\n GECİCİ1: (fazla boşluklar silindi)\n", gecici1)
			
		del pano_icerigi			# "pano_icerigi" listesini sil
		# # print("\nPano içeriği SİLindi:")
		
		for kelime in gecici1:	
			if kelime[-1] == "-":
				gecici2.append(kelime[:-1])
			
			elif kelime.startswith("\n"):
				gecici2.append(kelime[1:])
			
			elif "-\n" in kelime:
				gecici2.append(kelime.replace("-\n", ""))
			
			elif ".\n" in kelime:
				gecici2.append(kelime.replace(".\n", ".|"))	
			
			elif ";\n" in kelime:
				gecici2.append(kelime.replace(";\n", ";|"))
			
			elif ")\n" in kelime:
				gecici2.append(kelime.replace(")\n", ")|"))
			
			elif "\n\t" in kelime:
				gecici2.append(kelime.replace("\n\t", "\|\t"))
			
			else:
				gecici2.append(kelime)

		# # print("\n\nGEÇİCİ2 (-\\n, .\\n, ;\\n, \)\\n gecici degisim işlemleri yapıldı \) \n:", gecici2)
		
		gecici1.clear()
		# # print("gecici1 temizlendi:", gecici1)

		for kelime in gecici2:
			if "\n" in kelime:
				gecici1.append(kelime.replace("\n",""))
			
			elif ".|" in kelime:
				gecici1.append(kelime.replace(".|", ".\n"))
				
			elif ";|" in kelime:
				gecici1.append(kelime.replace(";|", ";\n"))

			elif ")|" in kelime:
				gecici1.append(kelime.replace(")|", ")\n"))
				
			elif "\|\t" in kelime:
				gecici1.append(kelime.replace("\|\t", "\n\t"))

			else:
				gecici1.append(kelime)
		
		# # print("\n\nGEÇİCİ 1  - enter komutları geri yüklendi:\n", gecici1)

		gecici2.clear()
		# # print("gecici2 temizlendi:", gecici2)
		
		metin = " ".join(gecici1)
		# # print(metin)
		
		gecici2 = metin.split("\t")
		# # print("TAB SPLİT\n", gecici2)
		
		duzenli = ""
		
		for kelime_grubu in gecici2:
			if kelime_grubu != "":
				duzenli += "\t" + kelime_grubu

		metin_kutusu.delete("1.0", tk.END)
		metin_kutusu.insert(tk.INSERT, duzenli)
		
		# # Düzenlenmiş Metni Panoya kopyalama kodu;
		# # duzenli = metin_kutusu.get(1.0, tk.END)
		pyperclip.copy(duzenli)
		
	else:		# Pano Boşsa, kopyalanmış metin yoksa;
		metin_kutusu.delete("1.0", tk.END)
		metin_kutusu.insert(tk.INSERT, "Panoya kopyalanmış metin bulunmamaktadır.")

metin_kutusu = tk.Text(
    width=40,
    height=10,
    wrap=tk.WORD
)
metin_kutusu.configure(font = ("Tahoma", 10))
metin_kutusu.pack(fill=tk.BOTH, expand=True)
    
buton_duzenle = ttk.Button(
    pencere,
    text="Kopyalanmış Metni  Düzenle ve Panoya Kopyala",
	style='TButton',	# Outline.TButton - primary, secondary, success, info, warning, danger, light, dark
    command= duzenle
)
buton_duzenle.pack(side='right', padx=10, pady=10)

pencere.mainloop()
