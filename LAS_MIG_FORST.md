# Malmö Klimatperspektiv 1.2.1 – rättning för GitHub och Streamlit

Version 1.2.1 rättar felet där Streamlit inte hittar `app/shell.html`.
Alla gränssnittsfiler och data finns nu samlade i `klimatperspektiv_data.json`.
Beräkningsmetod, cirkularitetsfunktioner och användarens styrning av boendeyta
per person och per hushåll är desamma som i 1.2.0.

## Uppdatera den befintliga appen

1. Packa upp huvudfilen `Malmo_Klimatperspektiv_1_2_1_Streamlit_fix.zip` på datorn.
2. Öppna det GitHub-repo som den befintliga Streamlit-appen använder.
3. Välj **Add file → Upload files**. Ladda upp just dessa tre uppackade filer
   direkt i repots huvudmapp, på samma nivå:
   - `streamlit_app.py` – ersätt den tidigare versionen.
   - `klimatperspektiv_data.json` – ladda upp hela filen.
   - `requirements.txt` – ersätt den tidigare versionen.
4. Spara med **Commit changes** på den gren som Streamlit-appen använder.
5. Kontrollera att startfilen i Streamlit är `streamlit_app.py`.
   Om appen fortfarande visar det gamla felet, starta om den med **Reboot app**.

Ladda upp filerna, inte huvud-ZIP-filen. De tre filerna ska ligga i samma mapp
och behålla sina namn. Ingen GitHub Action eller API-nyckel behövs.
Eventuella gamla mappar `app/` och `data/` kan ligga kvar; den nya
`klimatperspektiv_data.json` används när den finns bredvid startfilen.

Efter uppdateringen visar modellens versionsuppgift **1.2.1**.
Gamla scenarier kan läsas in på samma sätt som i 1.2.0.

## Öppna utan Streamlit

Öppna `Klimatperspektiv_Malmo_1_2_1.html` direkt i webbläsaren.
Beräkningar, gränssnitt och data ingår i filen. Bakgrundskartan kräver internet.

## Källkod och metod

`Kallkod_och_metod_1_2_1.zip` innehåller redigerbar källkod, metodtexter,
källförteckningar, exempel och tester. Den behöver inte laddas upp till GitHub
för att köra appen. Ändra källkoden där och kör `python tools/bygg_leverans.py UTKATALOG`
för att skapa en ny datafil och HTML-version efter ändringar.

## Verifiering

64 automatiska tester godkända: 52 tester av modellberäkningar och 12 av
data/sidbygge, varav åtta särskilt kontrollerar installation utan app- och datamappar.
Tre-filsversionen ger samma HTML-gränssnitt och samma nedladdningsbara underlag
som källkodsversionen. Publicering i ditt Streamlit-konto har inte utförts.
