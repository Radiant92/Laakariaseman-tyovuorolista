## User Storyt

## Työntekiöiden hallinta

### Hallinnon käyttäjänä haluan pystyä:

- Lisäämään työntekijöitä sovellukseen (complete)

- Nähdä listana kaikki työntekijät (complete)

- Asettaa työntekijälle salasanan (complete)

- Asettaa työntekijälle työnimikkeen lääkäri, sairaanhoitaja tai perushoitaja (complete)

- Muuttaa työntekijöiden aktiivista statusta (complete)

- Poistaa työntekijän

### Työntekijänä haluan pystyä:

- Kirjautumaan sovellukseen nimelläni ja salasanallani (complete)

- Muuttamaan oman salasanani

## Kiireellisyysluokat

### Hallinnon käyttäjänä haluan pystyä:

- Luoda kiireellisyysluokkia (complete)

- Asettaa kuhunkin luokkaan tarvittavan määrän kutakin työnimikettä (complete)

### Työntekijänä haluan pystyä:

- Näkemään kiireellisyysluokan nimen työviikossani (complete)

## Työviikot

### Hallinnon käyttäjänä haluan pystyä:

- Luoda työviikkoja (complete)

- Asettaa jokaisen työviikon jokaisen päivän jokaiseen tuntiin oman kiireellisyysluokan (complete)

- Asettaa tuntiin työntekijät (complete) 

- Poistaa tunnilta työntekijän (complete)

- vaihtaa tunnin kiireellisyysluokan (complete)

- Julkaista työviikon (complete)

- Viikkoa ei julkaista työntekijöille jos sen kiireellisyysluokkien vaatimukset ei ole täytetty (complete)

- Jos vaatimukset täyttyvät tunti näkyy työviikossa vihreänä(complete)

- Jos työntekijöitä on liika haluan että tunti näkyy purppurana(complete)

- Jos työntekiät eivät täytä luokan vaatimuksia luokan tulee näkyä punaisena ja vain hallinnolle(complete)

- Jos tunnilla on työntekijöitä muttei luokitusta niin tunti näkyy purppurana jossa lukee "luokaton"(complete)

- Jos tuntiin tulee muutoksia haluan että tunnin väritila muuttuu (complete)

- Katsella työviikkoja arkistosta (complete)

- Kirjauduttua haluan nähdä listan viikkoja joissa on ylimiehitystä (complete)

```
  ("SELECT distinct viikko.id, count(tunti.id) "
                    "FROM  tunti, paiva, viikko "                   
                    "WHERE viikko.id = paiva.viikko_id "  
                    "AND paiva.id = tunti.paiva_id "                    
                    "AND tunti.tila > 1 "                    
                    "GROUP BY viikko.id "                    
                    "ORDER BY viikko.id")
```
### Työntekijänä haluan pystyä:

- Katsella omia työviikkojani arkistosta (complete)
```
  "SELECT count(tunti.id), viikko.id, account.username "
		                "From viikko, paiva, tunti, tunti_user, account "
                    "WHERE viikko.id = paiva.viikko_id "
                    "AND paiva.id = tunti.paiva_id "
                    "AND tunti_user.tunti_id = tunti.id "
                    "AND account.id = tunti_user.account_id "
		                "AND tunti.tila > 0 "
		                "GROUP BY viikko.id, account.username"
```
- haluan että arkistossa näkyy myös montako tuntia minulla on siinä viikossa (complete) 

- En halua nähdä päiviä tai tunteja, jotka eivät kuulu minulle (complete)
```
"SELECT account.id, paiva.id From paiva, tunti, tunti_user, account "
                    "WHERE paiva.id = tunti.paiva_id "
                    "AND tunti_user.tunti_id = tunti.id "
                    "AND account.id = tunti_user.account_id "
                    "GROUP BY account.id, paiva.id"
```
