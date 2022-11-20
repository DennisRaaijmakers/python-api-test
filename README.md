# Project API
## Dennis Raaijmakers (r0894881)
## Klas: 2CCS01

## Beschrijving van het gekozen onderwerp
### Het onderwerp van mijn API is een video spel genaamd Rainbow Six Siege. In mijn API kun je informatie van een speler opvragen of een nieuwe speler maken en informatie van een operator opvragen. <br />

## Post request player
Bij de post request kun je een speler aanmaken. Je moet 5 waardes meegeven: de username, voornaam, achternaam, email en mmr. Dit moet je ingeven in een JSON formaat.
Voorbeeld van een body in JSON:
<pre>
{
    user_mame: "Player1",
    first_name: "Dennis",
    last_name: "Raaijmakers",
    email: "test@gmail.com"
    mmr: 3577
}
</pre>
Als je bij de user_name, first_name en last_name niks ingeeft dan wordt er "invalid" terug gegeven. Als je bij mmr geen cijfer meegeeft dan wordt het automatisch aangevuld naar een 0.
## Get request player
De informatie die je krijgt als je de speler opzoekt zijn: de username, voornaam, achternaam, email en mmr. 
Als je een lijst wilt met alle spelers kun je `/player/info/all` ingeven in de url.

De url die je gebruikt om een specifieke speler te zoeken is `/player/info/specific/{userName}` (met userName als een naam). Hier wordt gebruik gemaakt van een **path parameter**.

## Get request operator
De informatie die je krijgt van een operator zijn: opp_id, operatorName, primaryWeapon en secondaryWeapon.
Als je in de url `/opperator/info/all` ingeeft dan krijg je de informatie van alle operators.

Als je in de url `/opperator/info/specific/{opp_id}` (met opp_id als een nummer) ingeeft dan krijg je een specifieke operater die het id heeft die in de url meegegeven wordt. Hier wordt gebruik gemaakt van een **path parameter**.

Als je in de url `/opperator/info/query/random?amount=2` (de nummer 2 kun je aanpassen) ingeeft krijg je in dit geval 2 random operators te zien met hun opp_id, operatorName, primaryWeapon en secondaryWeapon. Hier wordt gebruik gemaakt van een **query parameter**. <br />

## Uitbreiding
Ik heb de website gestyled zodat de website er iets beter uitziet.<br />
Ook heb ik een post request op de website staan zodat je een speler kunt aanmaken die dan in de lijst verschijnt.
Ook heb ik gewerkt met een database. Ik heb sqlalchemy gebruikt als database.<br />

## Links API:
### Link naar hosted API: https://cloud.okteto.com/#/spaces/dennisraaijmakers?resourceId=624a4a53-30e9-4057-8f3c-cc56ec0ad131
### Link naar front end: https://github.com/DennisRaaijmakers/dennisraaijmakers.github.io
### Link naar hosted front end: https://dennisraaijmakers.github.io/

## Screenshot van werkende API
Hier zie je een screenshot van alle get en post requests:
![docs](images/docs_okteto.PNG) <br />

Hier kun je zien dat ik een speler aangemaakt heb via de website. Eerst klik je op submit om een player aan te maken en vervolgens druk je op de knop show players waarna dan alle spelers worden getoont, ook de speler die je zelf hebt aangemaakt.<br />
Op de website heb ik 2 get requests en 1 post request.<br />
Get request 1: een tabel met alle info over de spelers.<br />
Get request 2: een lijst van alle operators.<br />
post request: hier kun je een speler aanmaken.

![website post + werkende get request](images/post_request_website.PNG) <br />

Via postman kun je ook get en post requests uitvoeren. <br />
Je kunt alle operators opvragen, die worden dan getoont met hun uitrusting. <br />
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/opperators/info/all`
![postman all players](images/postman_all_operators.PNG) <br />

Je kunt ook een specifieke operator opvragen. Dit doe je door de operator id in te geven.<br /> 
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/opperators/info/specific/{opp_id}`
![postman specific player](images/postman_specific_operators.PNG) <br />

Als query parameter heb ik gekozen om verschillende operators random te tonen. Er kunnen geen dubbele komen want als je een getal meegeeft dat groter of gelijk is aan het aantal operators dan worden ze allemaal gegeven. Ook kun je niet hoger gaan als 60. <br /> 
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/opperators/info/query/random?amount=2`
![postman random players](images/postman_random_operators.PNG) <br />

Voor players heb ik ook een get request gemaakt die alle spelers met bijkomende info laat zien.<br />
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/players/info/all`
![postman all players](images/postman_all_players.PNG) <br />

Je kunt ook een specifieke speler opvragen door de voornaam van de speler in te geven. <br />
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/players/info/specific/Dennis`
![postman specific players](images/postman_specific_players.PNG) <br />

Via postman kun je ook een post request uitvoeren. <br />
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/players/create`
![postman post player](images/postman_post_request_1.PNG) <br />

Als je vervolgens een nieuwe specifieke request doet voor de speler dan kun je zien dat deze is toegevoegd.
Url: `https://api-service-dennisraaijmakers.cloud.okteto.net/players/info/specific/post`
![show postman post player](images/postman_post_request_2.PNG) <br />

Je kunt ook nog op de website checken of de speler toegevoegd is door weer op de knop show players te drukken.
![website posted player](images/post_request_website_2.PNG) <br />

## Bronnenlijst: 
https://technotrampoline.com/articles/building-an-ajax-form-with-alpinejs/ <br />
https://pages.github.com/ <br />
https://www.youtube.com/watch?v=0RqfzBRDWtk <br />
https://www.youtube.com/watch?v=NuDSWGOcvtg <br />
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax <br />