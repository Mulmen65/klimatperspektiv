# Malmö Klimatperspektiv 1.2.0

Öppna **Klimatperspektiv_Malmo_1_2.html** direkt i webbläsaren, eller använd GitHub/Streamlit med **streamlit_app.py** som startfil. Ladda upp mappens innehåll, inklusive app/, data/ och requirements.txt. Inga Actions eller API-nycklar behövs. Streamlit Cloud-publicering har inte testats i denna leverans.

## Nytt i cirkularitetsperspektivet
- Kortet visar undvikna utsläpp, negativt förändringsbidrag eller kvarvarande påverkan. Visningsvalet ändrar inte de faktiska utsläppen.
- Styrning via BOA per person eller BOA per hushåll, med personer/hushåll och BOA/BTA. Alternativets och referensens ytnivåer visas separat. Det tidigare BTA-läget finns kvar.
- Jämförelse för byggande och mark samt separata energi- och transportskillnader. Ingen extra subtraktion av samma besparing i totalen.
- Stegvis, ordningsberoende förklaring av vilka åtgärder som bygger upp besparingen.
- Avgränsad frivillig byggdelspost med CIRA:s köksinredningar som illustrativt exempel. Projektsiffror per kök, aldrig en generell faktor per m².
- Kartan och DeSO-kortet visar klimatnyttan relativt referensen, även när enskilda områden får högre belastning.

Se CIRKULARITET_1_2_METOD_OCH_REFERENSER.md och fliken Metod & källor för detaljerade formler, granskning av samtliga bilagor och nya litteraturkällor. Källkontroll beskriver verifieringsnivå och tillämpbarhet. Alla tidigare schabloner är inte dubbelverifierade. Bilagornas fulltexter medföljer inte i paketet.

## Inmatning
Välj Cirkularitet i menyn eller perspektivkortet. Ställ in ytenhet, hushållsstorlek och referens innan jämförelsen tolkas. BOA-lägen ersätter den procentuella ytminskningen; det procentreglaget visas bara i BTA-läget. Ytnivåerna avser tillkommande behov, inte automatisk anpassning av hela befintliga beståndet. Använd knappen för stegvis förklaring för att se hur åtgärder samverkar.

För verkliga byggdelar: fyll källa och avgränsning, välj DeSO, ange antal och jämförbara faktorer, välj bevarande och tidpunkt för eventuellt senare byte. CIRA-knappen är en demonstration, inte en Malmöinventering. För att ta bort exemplet: sätt antal till noll. Återställning återgår till hela modellens standardvärden.

## Gamla scenarier
1.1-inmatningar kan läsas in. Referensens hushållsstorlek har nu ett eget förval (2,11); den som tidigare ändrat hushållsstorlek bör kontrollera den nya referensen. Typologiläget är standard och bevarar 1.1-beräkningen utan nya åtgärder. Den nya komponenten byggdel är noll som standard. Resultatfiler har versionsnummer; spara version och scenario tillsammans.

## Kontroller
`node tests/test_model.js`, `node tests/test_upgrade.js`, `node tests/test_circular12.js`, `python -m unittest discover tests`. Se VALIDATION.md för utförda kontroller. Licenser i LICENSE gäller fortsatt. En fristående HTML-version innehåller redan koden och data och behöver ingen installation för beräkning. Bakgrundskartan kräver internet.

Byggdelsposten kräver separat aktivering efter kontroll av källa och avgränsning. CIRA-knappen fyller enbart indata och aktiverar inte posten i Malmötotalen. En demonstration är inte bekräftelse på att byggdelarna redan avskilts från andra klimatfaktorer.
