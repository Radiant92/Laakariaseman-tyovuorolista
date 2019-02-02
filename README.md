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
tai voit luoda täysin uuden työntekiän. 
tällä hetkellä kuka tahansa voi luoda työntekiän ja kaikilla on hallinto oikeudet, mutta luodut viikot näkyvät vain luojalle ja useampi käyttäjä ei voi luoda samalle viikolle viikkoa.

Kiireellisyysluokalla on täysi CRUD

# Linkit

Sovellus herokussa 
[sovellus](https://medi-tyovuorolista-harjoitus.herokuapp.com/)

[Tietokanta hahmotelma](https://github.com/Radiant92/Laakariaseman-tyovuorolista/blob/master/dokumentaatio/tietokantaHahmotelma.md)

[User Storyt](https://github.com/Radiant92/Laakariaseman-tyovuorolista/blob/master/dokumentaatio/userStoryt.md)

[Työloki](https://github.com/Radiant92/Laakariaseman-tyovuorolista/blob/master/dokumentaatio/timelog.md)
