# Kontroll av Malmö Klimatperspektiv 1.2.0
Datum: 2026-11-17.

22 ursprungliga beräkningstester, 12 tester för rättelserna i 1.1, 18 nya cirkularitetstester och 4 Pythonkontroller passerar: totalt 56.

Nya tester omfattar BOA/person kontra BOA/hushåll, BOA/BTA, frånvaro av dubbel ytminskning, tydlig referens, ytbalans, negativ besparing, DeSO-summering, faktisk total utan dubbel kredit, CIRA:s 18,55 ton, senare utbyteshändelse, avstängd post, källkrav, avgränsning, tidsordning, placering i DeSO, stegvis förklaring, visningsval och JSON-rundtur.

Chromiumkontroll: åtta vyer, area 30 mot 42, borttaget procentreglage i BOA-läge, oförändrad faktisk total vid byte av visning, sju steg i förklaringen och summa, cirkularitetskartans nyckeltal, inaktiv CIRA-demo, aktivering först efter avgränsningsval och referensskillnad 18,55 ton. Senare utbyte år 2040 ger −0,9 ton undviket under hela perioden. Inga JavaScript-fel i kontrollflödet. Visuell kontroll av cirkularitetsvyn genomförd.

Källgranskning och matematiska tester är inte oberoende extern validering av Malmös indata. Streamlit Cloud har inte startats eller publicerats här. Underlag och kvarstående verifieringsbehov från 1.1 redovisas i Källkontroll.
