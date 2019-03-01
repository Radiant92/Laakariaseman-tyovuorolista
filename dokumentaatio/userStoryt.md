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

## Työviikot

### Hallinnon käyttäjänä haluan pystyä:

- Luoda työviikkoja (complete)

- Asettaa jokaisen työviikon jokaisen päivän jokaiseen tuntiin oman kiireellisyysluokan (complete)

- Asettaa tuntiin työntekijät (complete) 

- Julkaista työviikon (complete)

- Viikkoa ei julkaista työntekijöille jos sen kiireellisyysluokkien vaatimukset ei ole täytetty (complete)

- Katsella työviikkoja arkistosta (complete)

- Kirjauduttua nähdä listan viikkoja joissa on ylimiehitystä (complete)

  ("SELECT distinct viikko.id, count(tunti.id) FROM  tunti, paiva, viikko "
                    "WHERE viikko.id = paiva.viikko_id "
                    "AND paiva.id = tunti.paiva_id "
                    "AND tunti.tila > 1 "
                    "GROUP BY viikko.id "
                    "ORDER BY viikko.id")

### Työntekijänä haluan pystyä:

- Katsella omia työviikkojani arkistosta (complete)

  ("SELECT distinct account.username, viikko.id From viikko, paiva, tunti, tunti_user, account "
                    "WHERE viikko.id = paiva.viikko_id "
                    "AND paiva.id = tunti.paiva_id "
                    "AND tunti_user.tunti_id = tunti.id "
                    "AND account.id = tunti_user.account_id")

- En halua nähdä päiviä tai tunteja, jotka eivät kuulu minulle (complete)

  ("SELECT account.username, paiva.id From paiva, tunti, tunti_user, account "
                    "WHERE paiva.id = tunti.paiva_id "
                    "AND tunti_user.tunti_id = tunti.id "
                    "AND account.id = tunti_user.account_id "
                    "GROUP BY tunti.id")
