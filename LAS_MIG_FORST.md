# Malmö Klimatperspektiv 1.3.0 – Cirkularitet: känslighet och osäkerhet

19 november 2026. Uppdatering av version 1.2.1.

## Uppdatera din befintliga GitHub/Streamlit-app

1. Packa upp detta paket.
2. Ladda upp och ersätt tre filer i GitHub-repots huvudmapp: `streamlit_app.py`, `klimatperspektiv_data.json` och `requirements.txt`.
3. Spara med Commit changes. Startfilen i Streamlit ska vara `streamlit_app.py`. Starta om appen vid behov.
4. Öppna Cirkularitet. Där finns den nya analysen. Kontrollera att versionsuppgiften är 1.3.0.

Ladda upp filerna, inte ZIP-filen. Ingen GitHub Action eller API-nyckel behövs.

För direkt granskning utan Streamlit: öppna `Klimatperspektiv_Malmo_1_3_0.html` i webbläsaren. Den innehåller hela modellen; bakgrundskartan behöver internet.

Knappen **Läs in beräknat exempel: Måttlig stegmodell** visar levererad analys med 1 000 dragningar och byter till exemplets modellantaganden. För egna scenarier: granska intervallen och välj **Beräkna känslighet och osäkerhet**. Osäkerhetsintervallen är villkorade analysantaganden, inte statistiskt verifierade Malmöintervall.

Metod, källor och exempelresultat: `CIRKULARITET_1_3_ANALYS_OCH_REFERENSER.md`.
Full redigerbar källkod, tester och råa exempeldragningar finns i `Kallkod_och_metod_1_3_0.zip`.

Tidigare sparade scenarier kan läsas in. Vid scenarioändring räknas analysintervallen om och analysen behöver köras igen. Ärvda schabloner behåller redovisade verifieringsbehov. Exakt input-/output-tokenstatistik för denna uppdatering är inte tillgänglig.

Beräknings- och paketeringstester har godkänts. Visuell webbläsarkontroll kunde inte utföras i arbetsmiljön. Appen är inte publicerad till ditt konto av denna leverans.
