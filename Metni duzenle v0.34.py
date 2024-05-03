import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import pyperclip

style = Style(theme='superhero')	# superhero, minty, lumen, sandstone, cerculean, simplex, morph, united, darkly, 

pencere = style.master
pencere.geometry("600x350+500+300")
pencere.title(".:: Metni Düzenle (v 0.34) - Mustafa Halil ::. ")

def metin_kutusundan_kopyala():
	duzenli = metin_kutusu.get(1.0, tk.END)
	pyperclip.copy(duzenli)

def metin_kutusuna_yapistir():
	pano_icerigi = pencere.clipboard_get().split(" ")
	print(pano_icerigi)
	
	gecici_cikti = ""
	nihai_cikti = ""
	
	if pano_icerigi != "":
		for kelime in pano_icerigi:
			if kelime == "":
				pano_icerigi.remove(kelime)
		
		for kelime in pano_icerigi:	
			if kelime[-1] == "-":
				gecici_cikti += kelime[:-1]
			
			elif ".\n" in kelime:
				gecici_cikti += kelime.replace(".\n", "|")
			
			elif "\n" in kelime:
				gecici_cikti += kelime.replace("\n"," ")
			
			else:
				gecici_cikti += kelime + " "
		
		for kelime in gecici_cikti:
			if "|" in kelime:
				nihai_cikti += kelime.replace("|", ".\n")
			
			else:
				nihai_cikti += kelime
		
		gecici_cikti = ""
					
		metin_kutusu.delete("1.0", tk.END)
		metin_kutusu.insert(tk.INSERT, nihai_cikti)
		
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
    text="Panodaki Metni  Düzenle",
	style='TButton',	# Outline.TButton - primary, secondary, success, info, warning, danger, light, dark
    command= metin_kutusuna_yapistir
)
buton_duzenle.pack(side='right', padx=10, pady=10)

buton_duzenlenmis = ttk.Button(
    pencere,
    text="Düzenlenmiş Metni Kopyala",
    style='TButton',	# Outline.TButton
    command= metin_kutusundan_kopyala
)
buton_duzenlenmis.pack(side='right', padx=10, pady=10)

pencere.mainloop()
