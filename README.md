# Siirtoäänivaali 2022

TKO-äly ry:n vuoden 2022 [äänestys- ja vaalijärjestyksen](https://www.tko-aly.fi/attachments/files/324/2022-12-28-_nestys-ja-vaalij_rjestys.pdf?1672444809) mukainen ääntenlaskuohjelma.

Ohjelma on valmis, mutta vaatii vielä testausta ja muiden tarkastelua.

Mikäli ajat ohjelmaa omalla koneella, luo samaan kansioon README-tiedoston kanssa kansio 'vaalit'. Tällöin ohjelma saa tallennettua laskenta- ja tulosdatan.

Ohjelma käynnistetään suorittamalla tiedosto app.py. Ohjelma kysyy käyttäjältä syötteenä OpaVotesta tekstimuodossa saatavan lipukedatan tiedostonimeä.

Ohjelma tulostaa laskentadataa kahteen tekstitiedostoon. Tiedosto, jonka nimi päättyy 'laskenta', sisältää tarkempaa dataa laskennan etenemisestä. Tiedosto, jonka nimi päättyy 'tulokset', sisältää laskennan tulokset lyhyemmässä muodossa, joka on helpompi esitellä esimerkiksi kokokseen osallitujille. Mikäli ääntenlaskun aikana tarvitsee ratkoa tasatilanteita pudotusvaiheessa, tiedostoja tulee useampi pari reskursiivisesti. Ensimmäisestä tiedostoparista löytyy ääntenlaskun lopullinen tulos.

## Ohjelman asentaminen

Kloonaa repositorio omalle koneellesi haluamaasi kansioon. 

Linuxilla esimerkiksi `~/Downloads`-kansioon asentaminen:

- Avaa komentorivi
- `cd ~/Downloads`
- `git clone https://github.com/mkkarl/Siirtoaanivaali2022.git`
- `cd Siirtoaanivaali2022`
- `mkdir vaalit`

OpaVotesta pitäisi saada jokaisesta vaalista tekstitiedoston ladattavaksi. 
Tallenna ne repositorion sisälle.

## Ohjelman ajaminen

Oletuksena, että ohjelma on asennettu `~/Downloads`-kansioon.

- Avaa komentorivi
- `cd ~/Downloads/Siirtoaanivaali2022`
- `python siirtoaanivaali2022/app.py`

Ohjelma pyytää lipukedatan tiedostonimeä. 
Kirjoita OpaVotesta lataamasi tiedoston nimi ja paina enteriä.
Ohjelma tekee kaksi tiedostoa `vaalit`-kansioon kutakin vaalia kohden.

## Havaitut ongelmat vaalijärjestyksessä

Valijärjestyksessä on havaittu joitain ongelmia. Niistä on kerrottu enemmän [täällä](dokumentaatio/havaitut_ongelmat.md).
