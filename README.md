# Siirtoäänivaali 2022

TKO-äly ry:n vuoden 2022 [äänestys- ja vaalijärjestyksen](https://www.tko-aly.fi/attachments/files/324/2022-12-28-_nestys-ja-vaalij_rjestys.pdf?1672444809) mukainen ääntenlaskuohjelma.

Ohjelma on valmis, mutta vaatii vielä testausta ja muiden tarkastelua.

Mikäli ajat ohjelmaa omalla koneella, luo samaan kansioon README-tiedoston kanssa kansio 'vaalit'. Tällöin ohjelma saa tallennettua laskenta- ja tulosdatan.

Ohjelma käynnistetään suorittamalla tiedosto app.py. Ohjelma kysyy käyttäjältä syötteenä OpaVotesta tekstimuodossa saatavan lipukedatan tiedostonimeä.

Ohjelma tulostaa laskentadataa kahteen tekstitiedostoon. Tiedosto, jonka nimi päättyy 'laskenta', sisältää tarkempaa dataa laskennan etenemisestä. Tiedosto, jonka nimi päättyy 'tulokset', sisältää laskennan tulokset lyhyemmässä muodossa, joka on helpompi esitellä esimerkiksi kokokseen osallitujille. Mikäli ääntenlaskun aikana tarvitsee ratkoa tasatilanteita pudotusvaiheessa, tiedostoja tulee useampi pari reskursiivisesti. Ensimmäisestä tiedostoparista löytyy ääntenlaskun lopullinen tulos.

## Havaitut ongelmat vaalijärjestyksessä

Valijärjestyksessä on havaittu joitain ongelmia. Niistä on kerrottu enemmän [täällä](dokumentaatio/havaitut_ongelmat.md).