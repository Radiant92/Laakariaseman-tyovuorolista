## käyttöohjeet

sovelluksen ladattuasi saat ohjelman käynnistetyksi

antamalla konsolissa komennot
1. pip install requirements.txt
2. python run.py
3. ja menemällä selaimessasi osoitteeseen http://localhost:5000/

päästyäsi aloitus sivulle valitse ylävalikosta kohta **Kirjaudu**

### Admin

Adminina eli sovelluksen hallitsijana sinun tulee aluksi kirjautua käyttäjänimellä **admin** ja salasanalla **admin**.
Huomaat että olet kirjautunut onnistuneesti ja kenen tunnuksilla olet kirjautuneena yläsarakkeen linkin **Kirjaudu ulos** jälkeisen sulkujen sisällä olevan tunnusnimen perusteella.

adminina kirjautuneena näet yläsarakkeella ruudun koon sallien joko rivin toimintoja tai pudotusvalikon.
Nämä tehtävät ovat työviikkojen katselua lukuunottamatta adminille vain tarkoitettuja ja muilta pois suljettuja toimintoja.

#### Lisää työntekijä
valitsemalla tämän sivulle avautuu uuden työntekiän luonti kaavake.
Kaavake validoi nimen ja salasanan lisäksi sen ettei käyttäjänimeä ole jo otettu käyttöön.
Tämän lisäksi admin asettaa uudelle käyttäjälle työnimikkeen "lääkäri", "sairaanhoitaja" ja "perushoitaja".
Nyt kirjattu käyttäjä voi jo itse kirjautua sovellukseen.

#### Lista työntekiöistä
Työntekijät listataan sivulle, josta erottuu heidän: **nimi**, **ammatti** ja **tila**.
tilan vieressä on nappi jossa lukee "**vaihda tila**", jonka toiminnallisuus tällähetkellä ei tee sen enempää kun vaihtaa käyttäjän tilan True ja False välillä.

#### Lisää kiireellisyysluokka
Kiireellisyysluokkia kannattaa tehdä edes yhden jos haluaa muuttaa tuntien tilaa, tästä pian lisää...
Luokalle tulee antaa nimi joka kuvaa hyvin tilannetta kuten "**punainen myrsky**" tai "**normi päivä**" joka myös validoidaan samannimisyydestä.
Luokalle annetaan myös lukumäärä lääkärejä, sairaanhoitajia ja perushoitajia jotka on miehitettävä.

#### Lista kiireellisyysluokista
Luotuasi muutaman kiireellisyysluokan voit nyt nähdä ne listattuna ja muokata napista niiden työntekiöiden määriä.
Jos taas haluat poistaa kiireellisyysluokan tämä onnistuu muokkaus napin viereisestä punaisesta poista napista.

#### Lisää työviikko
Tässä sinulta pyydetään vuosi ja viikko jolle haluaisit luoda työviikon. 
Viikon numeron valitset asettamalla kenttään numeron 1 - 52 välillä. 
Ota huomioon että viikon valittuasi voit muokata viikon vuotta ja numeroa tai poistaa viikon, mutta viikko vuosi kombinaatioita voi olla vain yksi järjestelmässä yhdenaikaisesti!

#### Lista työviikoista
**HUOM** jos poistat viikon niin siihen kuuluvat päivät ja tunnitkin poistuvat!

Aiemmassa kohdassa mainitsemani muokkaa ja poista löytyy tältä sivulta sekä viikon tietojen lisäksi ennen nappeja linkki nimeltä "**näytä**".

#### näytä
Painamalla linkkiä näytä avaat viikon näkymän.
Tässä näkymässä näet viikon ja vuoden, joiden alla suurehko taulukko jossa on kaikki viikon tunnit vasemmalla ja yläpuolella vastaavat viikonpäivät.
Taulussa näet punaisella "**luokaton**" kaikissa niissä tunneissa joille ei ole viellä määritelty luokitusta.
Jos taas tunnille on määritelty luokitus niin tämän luokituksen nimi näkyy tunnin kohdalla sinisenä tekstinä.
Jokatapauksessa molemmat tekstit toimivat linkkinä tunnin sivulle.

#### Tunti
Tunnin sivulla näet tällä hetkellä tunnin ajankohdan sekä mahdollisen kiireellisyysluokan nimen. 
keltaista muokkaa nappia painamalla pääset kaavakkeeseen joka mahdollistaa tunnille luokan asettamisen.

### Muuta
aivan ensimmäisenä asiana jonka kirjautuneena saatat huomata on lista työntekijöitä joilla ei ole viellä 40 työtuntia annettuna. Tämä ominaisuus tulee muuttumaan.

Kirjautuneena käyttäjälle jolla ei ole admin oikeuksia voit tällähetkellä ainoastaan nähdä viikot ja näille asetetut tunnit.
