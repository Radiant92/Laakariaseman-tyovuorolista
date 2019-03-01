## käyttöohjeet

sovelluksen ladattuasi saat ohjelman käynnistetyksi

antamalla konsolissa komennot
1. pip install requirements.txt
2. python run.py
3. ja menemällä selaimessasi osoitteeseen http://localhost:5000/

päästyäsi aloitus sivulle valitse ylävalikosta kohta **Kirjaudu**

4. jos et ole aiemmin käynnistänyt sovellusta niin tässävaiheessa viimeistään tiedosto db.users on rakentunut applikaatio kansioon.
5. kun olet löytänyt tiedoston avaa se komennolla sqlite3 users.db ja syötä komento **INSERT INTO account (name, username, password, job, active) values ('admin','admin','admin','ADMIN',1)**
6. kohtiin 'admin' voit täyttää haluamallasi tavalla kunhan neljäs 'ADMIN' on isolla kirjoitettu **ADMIN**
7. käynnistä palvelin uudestaan ja kirjaudu admin tunnuksillasi sovellukseen



### Admin

Adminina eli sovelluksen hallitsijana sinun tulee aluksi kirjautua käyttäjänimellä **admin** ja salasanalla **admin**.
Huomaat että olet kirjautunut onnistuneesti ja kenen tunnuksilla olet kirjautuneena yläsarakkeen linkin **Kirjaudu ulos** jälkeisen sulkujen sisällä olevan tunnusnimen perusteella.

adminina kirjautuneena näet yläsarakkeella ruudun koon sallien joko rivin toimintoja tai pudotusvalikon.
Nämä tehtävät ovat työviikkojen katselua lukuunottamatta adminille vain tarkoitettuja ja muilta pois suljettuja toimintoja.

Lisäksi heti kirjautuessasi sisään näet listan viikkoja joilla on ylimiehitystä, sekä ylimiehitettyjen tuntien määrän.

#### Lisää työntekijä
valitsemalla tämän sivulle avautuu uuden työntekiän luonti kaavake.
Kaavake validoi nimen ja salasanan lisäksi sen ettei käyttäjänimeä ole jo otettu käyttöön.
Tämän lisäksi admin asettaa uudelle käyttäjälle työnimikkeen "lääkäri", "sairaanhoitaja" ja "perushoitaja".
Nyt kirjattu käyttäjä voi jo itse kirjautua sovellukseen.

#### Lista työntekiöistä
Työntekijät listataan sivulle, josta erottuu heidän: **nimi**, **ammatti** ja **tila**.
tilan vieressä on nappi jossa lukee "**vaihda tila**", jonka toiminnallisuus tällähetkellä ei tee sen enempää kun vaihtaa käyttäjän tilan True ja False välillä, mutta tällä tulevaisuudessa voitaisiin asettaa käyttäjä "lomalle".

#### Lisää kiireellisyysluokka
Kiireellisyysluokkia kannattaa tehdä edes yhden jos haluaa muuttaa tuntien tilaa, tästä pian lisää...
Luokalle tulee antaa nimi joka kuvaa hyvin tilannetta kuten "**punainen myrsky**" tai "**normi päivä**" joka myös validoidaan samannimisyydestä.
Luokalle annetaan myös lukumäärä lääkäreitä, sairaanhoitajia ja perushoitajia, jotka on miehitettävä.

#### Lista kiireellisyysluokista
Luotuasi muutaman kiireellisyysluokan voit nyt nähdä ne listattuna ja **muokata** napista niiden työntekiöiden määriä.
Jos taas haluat poistaa kiireellisyysluokan tämä onnistuu muokkaus napin viereisestä punaisesta **poista** napista.

#### Lisää työviikko
Tässä sinulta pyydetään vuosi ja viikko jolle haluaisit luoda työviikon. 
Viikon numeron valitset asettamalla kenttään numeron 1 - 52 välillä. 
Ota huomioon että viikon valittuasi voit muokata viikon vuotta ja numeroa tai poistaa viikon, mutta viikko vuosi kombinaatioita voi olla vain yksi järjestelmässä yhdenaikaisesti!

#### Lista työviikoista
**HUOM** jos poistat viikon niin siihen kuuluvat päivät ja tunnitkin poistuvat!

Aiemmassa kohdassa mainitsemani **muokkaa** ja **poista** löytyy tältä sivulta, sekä viikon tietojen lisäksi ennen nappeja linkki nimeltä "**näytä**".

#### näytä
Painamalla linkkiä **näytä** avaat viikon näkymän.
Tässä näkymässä näet viikon ja vuoden, joiden alla suurehko taulukko jossa on kaikki viikon tunnit vasemmalla ja yläpuolella vastaavat viikonpäivät.
Taulussa näet punaisella "**luokaton**" kaikissa niissä tunneissa joille ei ole viellä määritelty luokitusta.
Jos taas tunnille on määritelty luokitus niin tämän luokituksen nimi näkyy tunnin kohdalla vihreänä tekstinä tai purppurana jos se sisältää *ylimiehitystä*.
Jokatapauksessa kaikki tekstit toimivat linkkinä tunnin sivulle.

#### Tunti
Tunnin sivulla näet tunnin ajankohdan sekä mahdollisen kiireellisyysluokan nimen, kaksi keltaista nappia ja listan tunnille asetettuja työntekiöitä. 
keltaista **vaihda luokkaa** nappia painamalla pääset kaavakkeeseen joka mahdollistaa tunnille luokan vaihtamisen.

Seuraava keltainen **lisää työntekijöitä** antaa sinun valita tunnille työntekijät listasta. Lopuksi lisäys vaatii allekirjoituksen.

Tässä vaiheessa jos olet lisäillyt luokan tai työntekijöitä näen värikoodatun punaisen, vihreän tai purppuran viestin joka kertoo nykyisen tunnin tilasta.
