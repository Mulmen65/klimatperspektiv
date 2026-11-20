# Klimatperspektiv 1.3.0 – känslighet och osäkerhet i Cirkularitet
19 november 2026. ÖP Malmö.

## Vad som har uppdaterats

Utgår från levererad version 1.2.1 (Malmo_Klimatperspektiv_1_2_1_Streamlit_fix.zip). Den befintliga Cirkularitetsvyn har kompletterats med en-parameteranalys, Monte Carlo, källredovisning och export. Samma beräkningsmotor, samtliga 209 DeSO och verkliga kapacitetstak används i varje körning. Den ordinarie modellens indata och grundresultat bevaras; nybyggnadens gemensamma analysmultiplikator har standardvärdet 1. Ingen publicering i användarens GitHub eller Streamlit har genomförts. Den tidigare Wordrapporten för 1.2.1 är inte uppdaterad av denna leverans.

## Användning i vyn

1. Öppna Cirkularitet. Välj det huvudscenario och den referens som ska prövas.
2. Öppna Intervall, fördelningar och källstöd. Granska lågt/grund/högt, fördelningar och vilka parametrar som varierar i simuleringen. Ange eget motiv eller källa när lokala data finns.
3. Välj analysperiod, antal dragningar, slumpfrö och korrelationsantagande. Analysperioden anges separat från huvudvyns årsval och är som förval ackumulerat 2025–2050.
4. Klicka Beräkna känslighet och osäkerhet. Analysen ändrar inte huvudscenariots indata. Avbryt-knappen lämnar inget ofullständigt resultat.
5. Växla mellan undvikna utsläpp och alternativets kvarvarande klimatpåverkan. Exportera analys/dragningar som JSON och känslighetstabellen som CSV. Hela modellens vanliga JSON-export innehåller också analysinställningar och eventuellt aktuellt analysresultat.
6. Knappen Läs in beräknat exempel byter till den levererade Måttlig stegmodellens samtliga grundantaganden och visar den förberäknade analysen med 1 000 dragningar. Spara eget scenario innan ett annat scenario läses in.

Vid ändrat huvudscenario återställs prövningsintervallen kring de nya grundvärdena och tidigare analysresultat markeras som inaktuella. Ändrad fördelning, intervall, period eller urval kräver omkörning. Vid import av modell-JSON återställs analysinställningarna; sparade resultat räknas om innan de används som aktuella. Åtgärdsfaktorer visas när motsvarande åtgärd är aktiv.

## Systemgräns, referens och beräkningsprincip

Ett jämförelsepar består av referensen utan cirkulära åtgärder och det valda alternativet. BOA-/hushållsreferensen hämtas från huvudscenariots explicita referensfält. Perioden 2025–2050 är en kalenderperiod för summering av bokförda flöden; den är inte en generell 50-årig livscykel. Årsresultat anges i ton CO₂e/år, ackumulerade i ton CO₂e. Diagram och kort räknar om till kt (1 kt = 1 000 ton).

För varje dragning j beräknas B_ref,j respektive B_alt,j som summan av modellens nybyggnad och rivning, anläggning, omvandling/påbyggnad/renovering, separat byggdel och förändrad markanvändning. Undviket_j = B_ref,j − B_alt,j. Positivt värde är lägre utsläpp än referensen; det är inte ett upptag ur atmosfären. Ingen ytterligare cirkularitetskredit subtraheras från faktiska utsläpp.

Energi och mobilitet redovisas som separata referensskillnader. Hela modellens skillnad = undviket byggande/mark + energiskillnad + mobilitetsskillnad i varje dragning. Percentiler av delposter är inte additiva. Referensens marginala P5/P95 får inte subtraheras från alternativets marginala P5/P95; skillnadsfördelningen räknas i varje par.

## Känslighet – en parameter i taget

Grundfallet beräknas först. För varje parameter görs ett fullständigt jämförelsepar vid den lägre gränsen och ett vid den högre; övriga parametrar hålls vid grundvärdet. Diagrammet visar ändringen mot grundfallet i kt CO₂e. Rangordningen använder största absoluta ändringen vid någon av ändpunkterna. Samtliga ändpunkter och parameterintervall finns i tabellen och CSV-filen. Procentuell ändring = 100 × största absoluta ändringen / absolutvärdet av grundresultatet; om grundresultatet är noll redovisas inget procenttal.

Rangordningen beror på valt prövningsintervall och är inte en fördelning av oberoende orsaksbidrag. Parametrar samverkar och kapacitetstak eller utbytesår kan skapa språng. Ändpunktsanalysen kartlägger inte alla inre extremvärden eller alla interaktioner. Den kompletteras därför av den samtidiga parameterprövningen, men är inte en Sobolanalys (European Commission, JRC, u.å.).

## Osäkerhet – Monte Carlo

Förval: 1 000 dragningar, slumpfrö 20261119, triangulära fördelningar med typvärde vid grundvärdet. Gränser och fördelningar är analysantaganden, inte empiriskt skattade Malmöfördelningar. Likformig fördelning kan väljas för varje parameter. En nollbredd ger ett konstant värde. Årtal använder heltalsgränser och avrundas efter dragning; detta ger en diskretiserad fördelning.

För triangulär fördelning med a = lägsta, c = typvärde, b = högsta och u likformigt i [0,1): om u < (c−a)/(b−a) används a + sqrt(u(b−a)(c−a)); annars b − sqrt((1−u)(b−a)(b−c)). För likformig används a + u(b−a). Seedad Mulberry32 används för reproducerbara dragningar; det är en numerisk generator, inte en kryptografisk funktion.

Samma dragna faktor används i referens och alternativ, över alla DeSO och år där parametern förekommer. Nybyggnadens multiplikator varierar alla byggnadstyper och årsvisa nivåer gemensamt, inklusive modellens automatiska småhusfaktorer och den del av påbyggnaden som beror på nybyggnadsfaktorn. Grundläggning, anläggning, omvandling och renovering har egna faktorparametrar. Faktorerna varierar inte oberoende mellan enskilda byggnader; detta är stadsgemensam parameterosäkerhet.

Åtgärdsval, referensval och befolkningsbana hålls som förval fasta i simuleringen, men prövas i en-parameteranalysen. Användaren kan välja att inkludera deras genomförandeosäkerhet. Befolkningsmultiplikatorn skalar förändringen från det faktiska basåret till varje milstolpe. Samma befolkningsbana används i jämförelseparet.

Grundantagandet är oberoende mellan olika osäkra parametrar. En separat inställning ger samma slumpkvantil för efOmv, efRenovering och pabFaktor. När faktorerna varierar innebär detta perfekt positiv rangsamvariation (+1), som en prövning av ett starkt gemensamt samband. Det är inte en skattad korrelation. Varje faktor är fortfarande identisk i referens och alternativ där den tillämpas. Övriga parametrar är oberoende.

P5, median och P95 beräknas med linjär interpolation mellan sorterade utfall, position (n−1)p. P5–P95 omfattar centrala 90 % av den antagna utfallsfördelningen. Intervallet är inte ett konfidensintervall för verkliga utsläpp. Andel positiv besparing avser bara dessa simuleringar; ett nästan numeriskt nollresultat (≤ 10⁻⁷ ton) räknas inte som positivt.

Spearmans rangkorrelation använder medelrang vid lika värden och redovisas bara när både indata och utfall varierar. Den mäter monoton samvariation, inte en kausal parameterandel eller ett Sobolindex. Halva och hela körningens P5/P95 visas som enkel kontroll av samplingsvariation, utan påstående om bevisad konvergens. Metoden stöds av JRC och ILCD; fördelningarnas faktaunderlag avgör tolkningens räckvidd (European Commission, JRC, u.å.; Wolf m.fl., 2011).

## Vilka antaganden som behöver lokalt underlag

Alla nya intervall och fördelningar har ursprungsetiketten ANALYTIKER26. De följande valen är exempel på känslighetsgränser och inte verifierade branschschabloner. Metodkällorna motiverar vilka samband som behöver prövas, inte de valda numeriska gränserna.

| Parameter i det levererade måttliga exemplet | Lägsta | Grund | Högsta | Enhet | I simuleringen som förval |
|---|---:|---:|---:|---|---|
| Nya invånare i befintligt bestånd | 0,00 | 5,00 | 15,00 | % | Fast |
| Minskad bostadsyta | 0,00 | 5,00 | 15,00 | % | Fast |
| Alternativets hushållsstorlek | 1,91 | 2,11 | 2,31 | personer/hushåll | Fast |
| Referensens hushållsstorlek | 1,91 | 2,11 | 2,31 | personer/hushåll | Fast |
| Minskad lokalyta | 0,00 | 10,00 | 20,00 | % | Fast |
| Andel omvandling | 0,00 | 10,00 | 20,00 | % | Fast |
| Andel påbyggnad | 0,00 | 5,00 | 15,00 | % | Fast |
| Renovering i stället för rivning | 40,00 | 50,00 | 60,00 | % | Fast |
| Andel återbruk | 0,00 | 10,00 | 20,00 | % | Fast |
| Kapacitet för omvandling | 5,00 | 10,00 | 15,00 | % av lokalbestånd | Ja |
| Kapacitet för påbyggnad | 2,50 | 5,00 | 7,50 | % av flerbostadshusens BTA | Ja |
| Klimatfaktor omvandling | 50,00 | 100,00 | 150,00 | kg CO₂e/m² BTA | Ja |
| Klimatfaktor renovering | 50,00 | 100,00 | 150,00 | kg CO₂e/m² BTA | Ja |
| Påbyggnad relativt nybyggnad | 0,50 | 0,70 | 0,90 | faktor | Ja |
| Besparing för den återbrukade andelen | 50,00 | 80,00 | 95,00 | % | Ja |
| Årlig rivnings- och ersättningstakt | 0,03 | 0,05 | 0,08 | %/år | Ja |
| Samtliga nybyggnadsfaktorer | 0,80 | 1,00 | 1,20 | multiplikator | Ja |
| Grundläggning | 13,00 | 26,00 | 39,00 | kg CO₂e/m² BTA | Ja |
| Gator och ledningar | 7,50 | 15,00 | 22,50 | kg CO₂e/m² mark | Ja |
| Extra anläggning vid förtätning | 0,00 | 0,00 | 0,00 | kg CO₂e/m² BTA | Fast |
| Klimatfaktor rivning | 3,50 | 7,00 | 10,50 | kg CO₂e/m² BTA | Ja |
| Kvarvarande kol under bebyggd mark | 11,00 | 22,00 | 33,00 | t C/ha | Ja |
| Andel av beräknad kolförlust som oxideras | 50,00 | 100,00 | 100,00 | % | Ja |
| Befolkningsbanans ökning från basåret | 0,75 | 1,00 | 1,25 | multiplikator | Fast |

Byggnadsdata, inventerade potentialer, faktisk BOA/BTA och åtgärdsomfattning behövs för att ersätta antaganden. Ärvda osäkra geografiska data, fullständig modellstruktur och alla framtidsbanor ingår inte i den kvantifierade spridningen.

Återbrukets nettobesparing bör tas från jämförbara funktioner med projektspecifika mängder, produktdata och relevanta transporter, spill, lager och rekonditionering (IVL, 2025; Boverket, u.å.). Den ärvda motorn begränsar besparingsfaktorn till 0–100 %. Den kan därför inte beskriva återbruk med större klimatpåverkan än nytillverkning. Detta är en uttrycklig modellbegränsning, inte en slutsats om sådana projekt.

Renoveringens bygginsats behöver bedömas tillsammans med framtida drift och livslängd. Galimshina m.fl. (2024) stöder relevansen av sådana osäkerheter, men använder schweiziska fall, andra systemgränser och en annan beräkningsmetod. Deras numeriska fördelningar har inte överförts hit.

## Genomförd exempelanalys

Endast det illustrativa scenariot Måttlig stegmodell används nedan. Inga specifika sparade användarindata identifierades i underlaget. Övriga värden är modellens grundvärden från 1.2.1. Ytstyrning är typologi; båda hushållsstorlekarna är 2,11. Måttlig: 5 % av nya invånare ryms i befintligt bestånd, 5 % lägre bostadsyta, 10 % mindre lokalyta, 10 % omvandling, 5 % påbyggnad, 50 % renovering i stället för rivning och 10 % återbruk. Dessa är modellval, inte beslutade Malmöåtgärder.

| Resultat, byggande och mark 2025–2050 | kt CO₂e |
|---|---:|
| Referens, grundfall | 1 314,44 |
| Alternativ, grundfall | 1 020,03 |
| Undviket, grundfall | 294,41 |
| Undviket, simulerad median | 288,24 |
| Undviket, P5 | 240,82 |
| Undviket, P95 | 334,27 |

Grundfallet är inte nödvändigtvis simuleringens median. Exempelvis är markOxidationens antagna intervall 50–100 med typvärde 100 och återbrukets besparing 50–95 med typvärde 80. Sådana fördelningar är asymmetriska, och hela modellen är inte linjär.

| Korrelationsprövning, 1 000 dragningar i vardera fallet | P5, kt CO₂e | Median, kt CO₂e | P95, kt CO₂e |
|---|---:|---:|---:|
| Oberoende parametrar | 240,82 | 288,24 | 334,27 |
| Gemensam rang för tre åtgärdsfaktorer | 240,06 | 288,00 | 336,97 |

Dessa två prövningar illustrerar bara två beroendeantaganden. De bevisar inte att andra samband saknar betydelse.

| Största en-parameterutslag för undvikna utsläpp | Prövat intervall | Största absolutändring mot grundfallet, kt CO₂e |
|---|---|---:|
| Referensens hushållsstorlek | 1,91–2,31 personer/hushåll | 94,05 |
| Nya invånare i befintligt bestånd | 0,00–15,00 % | 72,62 |
| Alternativets hushållsstorlek | 1,91–2,31 personer/hushåll | 72,24 |
| Andel återbruk | 0,00–20,00 % | 69,80 |
| Minskad bostadsyta | 0,00–15,00 % | 64,81 |
| Befolkningsbanans ökning från basåret | 0,75–1,25 multiplikator | 64,65 |
| Samtliga nybyggnadsfaktorer | 0,80–1,20 multiplikator | 59,84 |
| Andel omvandling | 0,00–20,00 % | 53,50 |

Referensens hushållsstorlek är det största en-parameterutslaget inom just dessa gränser. Det visar att jämförelsens referens behöver motiveras; det är inte ett bevis på en generell rangordning av kommunens åtgärder. Bland de indata som faktiskt varierar i Monte Carlo är nybyggnadsfaktorns gemensamma multiplikator starkast monotont samvarierande med besparingen i detta exempel. Rangkorrelation är inte osäkerhetsandel.

## Tidpunkt för bevarande och senare utbyte

Byggdelsposten är avstängd i Måttlig-exemplet. När den aktiveras och avgränsas prövar vyn även alternativets byte 2050 respektive 2051. CIRA-demonstrationens 30 kök ger 18,55 ton undviket när referensbyte är 2026, reparation 900 kg och nästa byte 2051; om samma nya kök även köps 2050 blir periodskillnaden −0,90 ton. Detta visar redovisningshorisontens effekt, inte en permanent utsläppsreduktion. CIRA:s användarbilaga är inte externt numeriskt verifierad.

## Verifiering och praktiska begränsningar

52 tidigare JavaScriptkontroller och 12 Pythonkontroller har passerat. 15 nya analyskontroller täcker bland annat identitet med huvudvyn, gemensamma faktorer utan falsk besparing, negativa resultat, småhusfaktor, byggdelspostens analytiska lösning, giltiga intervall, seed, fördelningar, percentiler, korrelation, reproducerbar fullmodell, korrelationsprövning och avbrott. Totalt 79 kontroller. Separat komponentflöde med DOM-stub provar demo, resultatmått, inaktuella resultat, inställningsimport, 200 simuleringar, exportobjekt och avbrott.

En faktisk visuell webbläsarkontroll kunde inte utföras: Chromium kunde inte starta eftersom miljön nekade dess socket. Komponenttestet ersätter inte visuell kontroll. Ingen ny skärmbild eller visuell verifiering påstås. Streamlit Cloud har inte startats eller publicerats här. Programtester verifierar logik och paketering, inte riktigheten i Malmös ursprungliga bestånds- och klimatdata.

## Tokenredovisning

Exakt antal input-token: inte tillgängligt. Exakt antal output-token: inte tillgängligt. Ingen fakturerings- eller usage-metadata för denna arbetssession tillhandahålls. Värdena lagras därför som null i analysens tokenUsage. De ska inte tolkas som noll eller som en uppskattning. Den lokala JavaScriptanalysen anropar ingen språkmodell.

## Referenser

European Commission, Joint Research Centre (u.å.). Methods: Global sensitivity analysis; Monte Carlo (or sample-based) analysis.
https://joint-research-centre.ec.europa.eu/sensitivity-analysis-samo/methods_en
Metodstöd för att ange intervall och fördelningar, dra parameteruppsättningar och analysera utfall. Stöd för att skilja global analys från en-parameterprövning.
Ingen Malmöparameter, sannolikhetsfördelning eller intervallgräns hämtas från källan. Webbsidan kontrollerad 2026-11-19.

Wolf, M.-A., Chomkhamsri, K., Brandão, M., Pant, R., Ardente, F., Pennington, D., Manfredi, S., de Camillis, C. och Goralczyk, M. (2011). International Reference Life Cycle Data System (ILCD) Handbook – General guide for Life Cycle Assessment – Detailed guidance. EUR 24708 EN. Publications Office of the European Union. doi:10.2788/38479.
https://publications.jrc.ec.europa.eu/repository/handle/JRC48157
Metodstöd: osäkerhetsfördelningar kräver underlag; metod- och scenarioval behöver separata beräkningar. Första upplagan av handboken är daterad mars 2010; hänvisningen avser JRC:s bibliografiska post 2011.
Publikationsmetadata och indexerat original i bilaga E kontrollerade 2026-11-19. Handboken styrker inte förvalda analysintervall.

Galimshina, A., Moustapha, M., Hollberg, A., Lasvaux, S., Sudret, B. och Habert, G. (2024). Strategies for robust renovation of residential buildings in Switzerland. Nature Communications, 15, 2227. doi:10.1038/s41467-024-46305-9.
https://www.nature.com/articles/s41467-024-46305-9
Stöd för att inkludera bygginsats, framtida energi, livslängd och andra osäkerheter vid renovering. Studien skiljer valbara åtgärder från exogena osäkra indata.
Schweiziska byggnader, 60 år och delvis annan systemgräns. Inga schweiziska faktorintervall överförs. Studien använder surrogatmodell/PCE; denna app använder fullmodell med Monte Carlo. Indexerad originaltext samt PubMed metadata kontrollerade 2026-11-19; direkt Nature-öppning gav inloggningsomdirigering.

IVL Svenska Miljöinstitutet (2025). Anvisningar för LCA-beräkning av byggprojekt. Version 2025–02, avsnitt 1.6.
https://magicbiblioteket.ivl.se/download/18.3d781b21194d85bfa42e8ab/1739194547290/Anvisningar%20f%C3%B6r%20LCA-ber%C3%A4kningar%20av%20byggprojekt%2C%20version%202025-02.pdf
Återbruk behöver belastas med relevant rekonditionering, transporter och byggprocess. En generell besparingsprocent måste ersättas av projektspecifik produktjämförelse när data finns.
Indexerat original, avsnitt 1.6, s. 20, kontrollerat 2026-11-19. Källan verifierar inte den ärvda schablonen 80 % eller det prövade intervallet 50–95 %.

Boverket (u.å.). Miljönytta cirkulärt byggande. Hämtad 19 november 2026.
https://www.boverket.se/sv/byggande/cirkular-ekonomi/cirkulara-byggnader/miljonytta/
Stöd för projektanpassad scenarioprövning och livscykelperspektiv; återbrukets klimatnytta varierar med metod, systemgräns och återbruksprocess.
Ingen generell återbruksprocent eller numerisk Malmöfördelning hämtas. Officiell sida kontrollerad 2026-11-19.

Klimatperspektiv, modellutveckling (2026). Prövningsantaganden för Cirkularitet, version 1.3.0, 19 november 2026.
Internt dokumenterade analysantaganden i denna leverans.
Ansvarig ursprungsetikett för samtliga nya intervall, fördelningsval, korrelationsantaganden och räkneexempel i denna uppdatering.
Antaganden för screening, inte empiriska skattningar, formell expertelicitering eller IVL-godkända schabloner. Egen källa eller motivering kan anges per parameter.

Övriga ärvda källor (BOV26, SCBBOA24, FISHMAN21, ALAUX24A, SLU25, MALMO25, IVL22, CIRA2 och ARVDA) redovisas med användning och begränsning i data/kallkontroll.json och den tidigare metodtexten CIRKULARITET_1_2_METOD_OCH_REFERENSER.md. Att en källa finns i registret innebär inte att den styrker de nya numeriska intervallen.
