# Lääkariaseman työvuorolista

Sovelluksen avulla hallitaan lääkärien, sairaanhoitajien ja perushoitajien työvuoroja.
Sovelluksen hallitsia voi hallita työntekjöitä ja kiireellisyysluokkia.
Sovellus antaa sen hallitsijan asettaa kullekkin viikonpäivän tunnille oman kiirreellisyys luokan ja sen vaatimat työntekijät.
kiireellisyysluokille voidaan määritellä tarvittava minimivahvuus jonka alittamista työviikkolistassa sovellus ei salli.

Työntekijä voi tarkastella omia työviikkojaan omasta arkistostaan
lääkäri voi tuurata sairaanhoitajaa tai perushoitajaa mutta sairaanhoitaja voi tuurata vain perushoitajaa. 

## Toimintoja

- Kirjautuminen
- Työntekiän hallinta
- Kiireellisyysluokkien hallinta
- Työvuorolistan hallinta
- Henkilökohtainen työvuoro lista
- Työvuorolistan listaus

## tunnus: admin, salasana: admin 
Vain admin voi luoda työntekijän joka saa tällä hetkellä hallinto oikeuden, muttei voi luoda samalle viikolle viikkoa.

Kiireellisyysluokalla on täysi CRUD

# Linkit

Sovellus herokussa, mutta sovellus ei käynnisty herokun kautta koska heroku ei anna sovellukseni tallentaa sinne tietokanta tauluja olen kokeillut tuhota ja luoda databasen uudelleen n. 10 kertaa ja rollbakkia sekä useita uudelleen deployayksia.
try/castchin poisto ei myöskään auttanut.

[sovellus](https://medi-tyovuorolista-harjoitus.herokuapp.com/)

[Tietokanta hahmotelma](https://github.com/Radiant92/Laakariaseman-tyovuorolista/blob/master/dokumentaatio/tietokantaHahmotelma.md)

[User Storyt](https://github.com/Radiant92/Laakariaseman-tyovuorolista/blob/master/dokumentaatio/userStoryt.md)

[Työloki](https://github.com/Radiant92/Laakariaseman-tyovuorolista/blob/master/dokumentaatio/timelog.md)
