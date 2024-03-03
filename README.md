# Metin_Düzenle

PDF dosyalarından, web sayfalarından, ...vb kaynaklardan kopyaladığımız metinleri Libre Ofis Writer, Microsoft Word, Gedit, Not Defteri, ...vb metin düzenleme  uygulamalarına yapıştırdığımız zaman, metinlerin satır yapısının, kayaktan kopyalandığı gibi olduğunu görürüz. 

Örnek bir **PDF** dosyası ve kopyalanan metnin **gedit** içerisine yapıştırıldığında karşılaştığımız sonuç aşağıdaki resimlerde görüntülenmektedir.

![pdf](img/01.png)

Kopyalanıp yapıştırılan metnin satır verileri, PDF dosyasındaki içerikle ile aynı ve aynı sayıda karakter içeriyor.   Toplam 20 satır veri var.

![gedit1](img/02.png)

Metni bu şekilde kopyalayarak Tercüme (translate) uygulamalarına yapıştırısak, cümle bütünlüğü sağlanmadığı için yanlış tercüme elde ederiz. Bizim yapmak istediğimiz şey, bu içerikteki satırları ardarda getirme, "varsa" bir kısmı alt satıra taşmış kelimeleri birleştirmek ve her bir cümleyi ayrı bir satıra gelecek şekilde düzenleyen python kodunu yazmak.

> Kodun doğru çalıması için;
> 
> Düzenlemek istediğiniz metni, kod ile aynı klasöre (dizine), **metin.txt** ismi ile kaydedin ya da kod içerisindeki `txt_dosya = "metin"` kısmını değiştirin.

Kodu çalıştırdığınızda, aynı dizin (klasör) içerisinde **metin_duzenlendi.txt** isminde yeni bir dosya oluşturulacaktır. İçerik, toplam 13 satır veri (cümle) haline geldi.

![gedit2](img/03.png)

**metin_duzenlendi.txt** dosyasını incelerseniz, içerikteki bir kısmı alt satıra taşmış kelimelerin birleştirildiğini ve her bir cümlenin ayrı bir satıra gelecek şekilde düzenlendiğini görebilirsiniz.

Gedit programının yatay boyutunu artırsak ta cümle bütünlüğünün korunduğunu görebiliriz. Metni bu şekilde kopyalayarak Tercüme (translate) uygulamalarına yapıştırısak, cümle bütünlüğü sağlanmış olur.

![gedit4](img/04.png)
