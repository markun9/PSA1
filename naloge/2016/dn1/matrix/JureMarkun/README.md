# Poročilo

Jure Markun

********************************************
*Napišite tudi poročilo, v katerega vključite sledeče:

Kratek opis vaših algoritmov.
Natančna analiza časovne in prostorske zahtevnosti vaših algoritmov v odvisnosti od dimenzij vhodnih matrik.
Primerjava dejanskih časov izvajanja vaših algoritmov pri vhodih različnih velikosti.
Poročilo imate lahko kar v datoteki README.md v mapi z vašimi programi (v obliki Markdown), lahko pa naredite tudi poročilo v LaTeXu (na repozitorij naložite datoteko .tex - datoteke .pdf so izključene v .gitignore in jih torej ne nalagajte).
*******************************************

1.SlowMatrix

Prva vrsta množenja matrik, ki ga poznamo, je naivno množenje. To je običajno množenje matrik, kjer vrstice leve matrike množimo z stolpci desne in produkte seštevamo. Za implementacijo tega algoritma je poleg preverjanja ustreznosti dimenzij matrik potrebna le for zanka, ki gre skozi koeficiente obeh prvotnih matrik in zmnožke zapiše v ciljno matriko.

*Prostorska zahtevnost*
Prostor, ki ga algoritem porabi je enak O(nm + ml + nl) =< O(3max(nm,ml,nl)) =< O(3max(n^2,m^2,l^2)), ker porabi zgolj prostor za vhodne matrike ter O(1) za konstante, ki so dimenzije teh matrik.
*Časovna zahtevnost*
Časovna zahtevnost algoritma je enaka O(mln). Mest v ciljni matriki je nxl, za vsako mesto pa algoritem izvede m množenj (seštevanja nimajo velikega vpliva). Za majhne matrike je to sprejemljivo, za večje pa je algoritem počasen in neučinkovit.

Kot osnoven primer vzemimo, matriko oblike (n,m,l) = (51,23,45). V tem primeru algoritem izvede kar 52785 množenj.

2.FastMatrix

To matriko sem vzel kot vmesno stopnjo po hitrosti od SlowMatrix in FastMatrix.
