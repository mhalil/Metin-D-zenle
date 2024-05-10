import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import pyperclip, re

style = Style(theme='minty')	# superhero, minty, lumen, sandstone, cerculean, simplex, morph, united, darkly, 

pencere = style.master
pencere.geometry("850x425+400+200")
pencere.title(".:: Metni Düzenle (v 0.35) - Mustafa Halil ::. ")

def metin_kutusundan_kopyala():
	duzenli = metin_kutusu.get(1.0, tk.END)
	pyperclip.copy(duzenli)

def metin_kutusuna_yapistir():
	pano_icerigi = pencere.clipboard_get().split(" ")
	
	gecici_pano = []
	gecici_cikti = ""
	nihai_cikti = ""
	
	if pano_icerigi != "":
		
		for kelime in pano_icerigi:
			
			if kelime != "":
				gecici_pano.append(kelime)
				
		del pano_icerigi			# "pano_icerigi" listesini sil
		
		for kelime in gecici_pano:	
			if kelime[-1] == "-":
				gecici_cikti += kelime[:-1]
			
			elif ".\n" in kelime:
				gecici_cikti += kelime.replace(".\n", ".|")
			
			elif ";\n" in kelime:
				gecici_cikti += kelime.replace(";\n", ";é")
			
			elif "\n" in kelime:
				gecici_cikti += kelime.replace("\n"," ")
			
			else:
				gecici_cikti += kelime + " "
		
		for kelime in gecici_cikti:
			if "|" in kelime:
				nihai_cikti += kelime.replace("|", "\n")
			
			elif "é" in kelime:
				nihai_cikti += kelime.replace("é", "\n")
				
			else:
				nihai_cikti += kelime
		
		gecici_cikti = ""
					
		metin_kutusu.delete("1.0", tk.END)
		metin_kutusu.insert(tk.INSERT, nihai_cikti)
		
		# Düzenlenmiş Metni Panoya kopyalama kodu;
		duzenli = metin_kutusu.get(1.0, tk.END)
		pyperclip.copy(duzenli)
		
	else:
		metin_kutusu.delete("1.0", tk.END)
		metin_kutusu.insert(tk.INSERT, "Panoya kopyalanmış metin bulunmamaktadır.")

yazitipi_ozelligi = ("Tahoma", 10)	# ("Tahoma", 10, "bold")

metin_kutusu = tk.Text(
    width=40,
    height=10,
    wrap=tk.WORD
)
metin_kutusu.configure(font = yazitipi_ozelligi)
metin_kutusu.pack(fill=tk.BOTH, expand=True)
    
buton_duzenle = ttk.Button(
    pencere,
    text="Kopyalanmış Metni  Düzenle ve Panoya Kopyala",
	style='TButton',	# Outline.TButton - primary, secondary, success, info, warning, danger, light, dark
    command= metin_kutusuna_yapistir
)
buton_duzenle.pack(side='right', padx=10, pady=10)

# #buton_duzenlenmis = ttk.Button(
    # #pencere,
    # #text="Düzenlenmiş Metni Kopyala",
    # #style='TButton',	# Outline.TButton
    # #command= metin_kutusundan_kopyala
# #)
# #buton_duzenlenmis.pack(side='right', padx=10, pady=10)

pencere.mainloop()
