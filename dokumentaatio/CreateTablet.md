### Tietokannan Create Tablet
Herokussa tietokanta on Postgre
```
CREATE TABLE kiireellisyysluokka (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        laakarit INTEGER NOT NULL, 
        sairaanhoitajat INTEGER NOT NULL, 
        perushoitajat INTEGER NOT NULL, 
        PRIMARY KEY (id)
);
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        job VARCHAR(144) NOT NULL, 
        active BOOLEAN NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (active IN (0, 1))
);
CREATE TABLE viikko (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        vuosi INTEGER NOT NULL, 
        numero INTEGER NOT NULL, 
        PRIMARY KEY (id)
);
CREATE TABLE paiva (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        tila BOOLEAN NOT NULL, 
        name VARCHAR(144) NOT NULL, 
        viikko_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (tila IN (0, 1)), 
        FOREIGN KEY(viikko_id) REFERENCES viikko (id)
);
CREATE TABLE tunti (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        tunti INTEGER NOT NULL, 
        paiva_id INTEGER NOT NULL, 
        luokka_id INTEGER, 
        tila INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(paiva_id) REFERENCES paiva (id), 
        FOREIGN KEY(luokka_id) REFERENCES kiireellisyysluokka (id)
);
CREATE TABLE tunti_user (
        account_id INTEGER, 
        tunti_id INTEGER, 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(tunti_id) REFERENCES tunti (id)
);
```

