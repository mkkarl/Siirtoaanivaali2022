# Havaitut ongelmat TKO-äly ry:n vaalijärjestyksessa

Ohjelman koodaamisen yhteydessä on havaittu joitakin ongelmia [vaalijärjetyksessä](https://www.tko-aly.fi/attachments/files/324/2022-12-28-_nestys-ja-vaalij_rjestys.pdf?1672444809). Vaalijärjestys on kirjoitettu pohjautuen [Meekin metodiin (Meek's method)](https://svn.apache.org/repos/asf/steve/trunk/stv_background/meekm.pdf), mutta äänikynnyksenä on käytetty [Droopin äänikynnyksen (Droop quota)](https://en.wikipedia.org/wiki/Droop_quota) sijasta [Haren äänikynnystä (Hare quota)](https://en.wikipedia.org/wiki/Hare_quota). Vaalijärjestystä kirjoitettaessa ei kuitenkaan ole suoritettu kunnollista testausta ääntenlaskennan kannalta ja vvalijärjestykseen on päätynyt joitakin ongelmakohtia siihen liittyen. Tällä sivulla kerrotaan ongelmista ja niiden ratkaisuehdtuksista.

## Ehdokkaiden valinnan ja pudotuksen ajankohta

Vaalijärjestyksessä ei ole selkeästi määritetty kohtaa, jossa äänikynnyksen ylittäneiden ehdokkaiden valinta tapahtuu.

**Ratkaisuehdotus:** Vaalijärjestyksessä on ääntenlaskun suorittamisessa kohdat 1-4. Suoritetaan ehdokkaiden valinta kohtien 3 ja 4 välissä. Tällöin ehdokkaiden valintaan käytetty äänikynnys ja lasketut äänet ovat samalta laskentakierrokselta.

Jos kierroksella ei valita ehdokkaita, suoritetaan ehdokkaiden pudotus ~~kohdan 4 jälkeen~~ myös kohtien 3 ja 4 välissä.

Vaalijärjestystä voi tulkita, että pudotus tulisi suorittaa kohdan 4 jälkeen. p-arvon päivittäminen ei kuitenkaan vaikuta pudottamiseen. Mikäli päädytään seuraavassa kohdassa kuvattuun p-arvon laskemiseen, koodin kannalta on helpompi, jos sekä valinta että pudottaminen suoritetaan kohtien 3 ja 4 välissä.

## p-arvon laskeminen

Vaalijärjestyksen mukainen p-arvon laskeminen aiheuttaa välillä tilanteen, jossa valituilla ehdokkailla on ääniä enemmän kuin äänikynnyksen verran.

**Ratkaisuehdotus:** Lasketaan artikkelin [Algorithm 123 — SINGLE TRANSFERABLE VOTE BY MEEK’S METHOD (Hill, et al. 1987)](https://svn.apache.org/repos/asf/steve/trunk/stv_background/meekm.pdf) mukaisesti äänikynnykselle, painolle p, kokonaisäänimäärille ja äänihukalle uusi arvo, kuten on kuvattu artikkelin kohdassa 2.9.

Toteutetaan tämä siten, että toistetaan vaalijärjestyksessä kuvattuja kohtia 1-4. Kohdan 3 jälkeen tarkistetaan valittujen ehdokkaiden kokonaisäänimäärien ja äänikynnyksen suhdeluku. Jos suhdeluku on kaikilla valituilla ehdokkailla määrätyissä rajoissa, suoritetaan valinta tai tarvittaessa kohdan 4 jälkeen pudotus. Mikäli suhdeluku ei ole määrätyissä rajoissa, ei suoriteta valintaa eikä pudotusta vaan ainoastaan kohta 4 ja siirrytään takaisin kohtaan 1.

## Ehdokkaan valinta äänikynnyksen ylittyessä

Vaalijärjestyksen mukaan ehdokkaan tulee *ylittää* äänikynnys tullakseen valituksi eli ehdokkaan kokonaisäänimäärän tulee olla suurempi kuin äänikynnys. Koska äänikynnys lasketaan

*(kaikki hyväksytyt äänet - yhteenlaskettu äänihukka) / valittavien paikkojen määrä*,

niin ainakin viimeinen valittavissa oleva ehdokas ei ylitä äänikynnystä, vaan saavuttaa sen juuri ja juuri tai jää hieman sen alapuolelle riippuen pyöristyksistä. Mikäli p-arvon laskemiseen ei tehdä korjausta, ongelma on vielä huomattavampi.

**Ratkaisuehdotus:** Kun ehdokkaiden valitsemisten ja pudottamisten jälkeen jäljellä on enää vapaiden paikkojen verran toiveikkaita ehdokkaita, valitaan jäljellä olevat toiveikkaat ehdokkaat.