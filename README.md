# Project API
## Dennis Raaijmakers (r0894881)
## Klas: 2CCS01

## Beschrijving + links
### Het onderwerp van mijn API is een video spel genaamd Rainbow Six Siege. In mijn API kan je informatie van een speler opvragen of een nieuwe speler maken en informatie van een opperator opvragen.

## Post request player
Bij de post request kan je een speler aanmaken. Je moet 5 waardes meegeven: de username, voornaam, achternaam, email en mmr. Dit moet je ingeven in een JSON formaat.
Voorbeeld van een body in JSON:
<pre>
{
    userName: "Player1",
    firstName: "Dennis",
    lastName: "Raaijmakers",
    email: "test@gmail.com"
    mmr: 3577
}
</pre>
## Get request player
De informatie die je krijgt als je de speler opzoekt zijn: de username, voornaam, achternaam, email en mmr van de speler. 
Als je een lijst wilt met alle spelers kan je **/player/info/all** toe te voegen aan de url. Hier wordt gebruik gemaakt van een path parameter.

De url die je gebruik om een specifieke speler te zoeken is **/player/info/specific/{userName}** (met userName als een naam). Hier wordt gebruik gemaakt van een query parameter.

## Get request opperator
De informatie die je krijgt van een opperator zijn: opp_id, opperatorName, primaryWeapon en secondaryWeapon.
Als je in de url **/opperator/info/all** ingeeft dan krijg je de informatie van alle opperators. Hier wordt gebruik gemaakt van een path parameter.

Als je in de url **/opperator/info/specific/{opp_id}** (met opp_id als een nummer) dan krijg je een specifieke opperater die het id heeft die in de url meegegeven wordt. Hier wordt gebruik gemaakt van een query parameter.

## uitbreiding
Ik heb de website gestyled zodat de website er iets beter uitziet.
Ook heb ik gewerkt met een database ik heb ik sqlalchemy gebruikt.

## Links API:
### Link naar hosted API:
### Link naar front end: https://github.com/DennisRaaijmakers/dennisraaijmakers.github.io
### Link naar hosted front end: https://dennisraaijmakers.github.io/

## Screenshot van werkende API



## Bronnenlijst: 
https://technotrampoline.com/articles/building-an-ajax-form-with-alpinejs/ <br />
https://pages.github.com/ <br />
https://www.youtube.com/watch?v=0RqfzBRDWtk <br />
https://www.youtube.com/watch?v=NuDSWGOcvtg <br />