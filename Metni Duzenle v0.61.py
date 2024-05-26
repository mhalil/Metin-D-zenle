import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import pyperclip, re

style = Style(theme='minty')	# superhero, minty, lumen, sandstone, cerculean, simplex, morph, united, darkly, 

pencere = style.master
pencere.geometry("850x425+400+200")
pencere.title(".:: Metni Düzenle (v 0.61) - Mustafa Halil ::. ")


def duzenle():
	pano_icerigi = pencere.clipboard_get()
	# # print("PANO İÇERİĞİ:", type(pano_icerigi))
	
	with open("gcc.txt", "w", encoding = "utf-8") as dosya:
		dosya.write(pano_icerigi)
	
	with open("gcc.txt" , "r", encoding="utf-8") as icerik:
		satirlar = icerik.readlines()
		# # print(satirlar)
		
		metin = ""
		
		for satir in satirlar:
			if satir == "\n":
				metin += satir * 2		# paragraflar arasında 1 adet boş satır bulunsun
			elif satir[-2:] == "-\n":
				metin += satir[:-2]
			
			elif satir[-1:] == "\n" and satir[-2:] != "-\n":
				metin += satir[:-1] + " "			
			
			else:
				metin += satir
		
		# # print("\nMETİN1:\n", metin)
		
		del satirlar			# "satirlar" listesini sil

		metin_kutusu.delete("1.0", tk.END)
		metin_kutusu.insert(tk.INSERT, metin)
		
		# # Düzenlenmiş Metni Panoya kopyalama kodu;
		pyperclip.copy(metin)
		

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
