# Cirkularitet i Malmö Klimatperspektiv 1.2

## Resultatets innebörd
Cirkularitetskortet visar hur mycket lägre eller högre klimatpåverkan alternativet ger jämfört med en uttrycklig referens. Tre visningar finns: undvikna utsläpp (positiv besparing), förändringsbidrag (negativt vid besparing) och kvarvarande påverkan. De är tre redovisningar av samma jämförelse och ändrar inte beräkningen.

Undviket = E_referens − E_alternativ.
Förändringsbidrag = E_alternativ − E_referens.
E_alternativ = E_referens + förändringsbidrag.

Detta är jämförelsebokföring, inte fysisk kolinlagring eller negativa utsläpp genom upptag ur atmosfären. Modellen använder ingen sådan borttagning i denna modul. Lägre nybyggnadsmängd och återbruk sänker redan faktiska byggutsläpp. Undviket utsläpp får därför inte dessutom dras av från alternativets totalsumma. Inte heller får komponentbesparingar summeras med hela byggnadens besparing om samma byggdel ingår i båda.

Huvudmåttet omfattar byggande, separat anläggning, omvandling, påbyggnad, renovering, eventuell separat byggdelspost och förändrad markanvändning. Byggande och mark visas även var för sig. Energi, transport och skillnaden för hela modellens omfattning visas separat. Jämförelsen är varken fullständig byggnads-LCA eller verifierat klimatbokslut. Alla kvarstående begränsningar från 1.1 finns kvar om de inte uttryckligen ändrats här.

## Forskningens roll
Forskningen motiverar att först pröva ytbehov, bättre nyttjande och bevarande, sedan omvandling och materialval. Alaux m.fl. (2024a, tabell 1) och Fishman m.fl. (2021, figur 2 och scenariometod) kopplar servicebehov till bestånd och fysiska flöden. Ness (2022; 2023) bidrar med syntes och policyanalys, inte empiriska lokala reduktionsfaktorer. Nick (2024) är ett normativt systemscenario med en egen avgränsning av privata och gemensamma ytor. Hansen m.fl. (2023) behandlar andra systemgränser och tidshorisonter än Malmömodellen. Dessa resultat läggs därför inte in som en schablonmässig utsläppsrabatt.

I Alaux m.fl. (2024b, avsnitt 2.4) jämförs 44 m²/person med en framtida referens på 55,3, medan utgångsläget är cirka 46. Det illustrerar hur referensvalet ändrar besparingen. Cirka 20 % lägre yta än referensen innebär inte 20 % mindre yta än dagens nivå, och artikelns beräknade utsläppsminskningar är inte automatiskt samma procent som ytminskningen.

## Yta per person och hushåll
Användaren väljer ett styrande inmatningssätt:
1. BTA per byggnadstyp, enligt tidigare version, med separat procentuell ytminskning.
2. BOA per person och personer per hushåll.
3. BOA per hushåll och personer per hushåll.

BOA_hushåll = BOA_person × personer_hushåll.
BTA_hushåll = BOA_hushåll / BOA_andel_av_BTA.

Den icke styrande ytenheten räknas fram och visas direkt. De två ytvärdena multipliceras aldrig som två oberoende effekter. Procentreglaget för mindre bostadsyta används bara i det tidigare BTA-läget. Omräkningens standard 0,8 är ett ändringsbart antagande och ska ersättas med lokalt projektunderlag. BOA, BTA, Atemp och utländska mått på floor area är olika storheter.

Den önskade genomsnittliga BTA:n fördelas i BOA-lägena proportionellt på de valda typologiernas BTA. Relationen mellan flerbostadshus och småhus bevaras; typblandningen följer användarens val. Om den ändrade BTA:n påverkar småhusets uppskattade Atemp kan modellens automatiska klimatfaktor också ändras. Det är ett synligt tröskeleffektantagande som kan prövas med egna klimatfaktorer.

Ytvalet gäller tillkommande bostadsbehov under perioden. Det inför inte automatiskt ett mål för hela befintliga bostadsbeståndets BOA/person. Bättre nyttjande av befintligt bestånd styrs fortfarande av dess separata parameter. Minskad yta behöver bedömas tillsammans med trångboddhet, boendekvalitet, hushållssammansättning och gemensamma ytor (CIRA2; Nick, 2024). Ett genomsnittligt ytmått mäter inte fördelningen mellan hushåll.

## Referensen
Referensen är synlig och redigerbar med egen ytenhet, egen BOA per person/hushåll och egen hushållsstorlek. I typologiläget används samma byggnadstyper och BTA per typ som i alternativet, före procentuell ytminskning. Vill användaren låsa en historisk genomsnittsarea när typologierna ändras bör referensen anges som absolut BOA.

Samma befolkningsbana, tidsperiod, externa klimatfaktorer och lokaliseringsregler används. Referensens åtgärdsandelar för ytminskning, inflyttning i befintligt bestånd, mindre lokalyta, omvandling, påbyggnad, renovering i stället för rivning och materialåterbruk sätts till noll. Referensen behandlar den frivilliga byggdelsposten som utbyte utan bevarande.

Ändrad hushållsstorlek är ett självständigt scenarioantagande. Det kan ändra både antalet bostäder och modellens bilvolym för nya hushåll. Målbefolkningen hålls lika, men en likvärdig boendekvalitet kan inte antas enbart därför att antalet personer är lika. Referensen är en modelljämförelse, inte ett observerat kontrafaktiskt förlopp.

## Besparingarnas placering
Nybyggnadens mängd beräknas efter ytval och efter omvandling/påbyggnad. Därmed minskar byggpåverkan i Nyexploatering direkt. Förtätning, markanspråk och nya byggnaders energi följer de ändrade mängderna enligt befintlig motor. Cirkulära insatsers faktiska utsläpp ligger kvar som positiva flöden i respektive år. Cirkularitetens klimatnytta är skillnaden mellan två kompletta, jämförbara körningar.

Kartans cirkularitetslager och områdeskort visar undviket byggande och mark per DeSO. Positiva tal betyder besparing. Negativa tal och röd färg visar att påverkan ökar i området. Det kan bero på att byggande flyttas mellan platser. Områdesvärden summerar till stadens jämförelse. Kartlagret ska inte summeras med de faktiska utsläppslagren.

Knappen för stegvis förklaring beräknar skillnaden i en fast följd: ytbehov/hushållsstorlek, befintligt bestånd/lokalyta, omvandling, påbyggnad, renovering, materialåterbruk, separat byggdelsbevarande. Summan av stegskillnaderna är exakt skillnaden mellan referens och slutligt alternativ, även när vissa steg ökar utsläppen. Åtgärder samverkar, så fördelningen mellan stegen är ordningsberoende och är inte oberoende effektskattningar eller Shapleyvärden.

## Byggdelsbevarande och CIRA-exempel
CIRA-processen 2.0 visar bland annat värdet av att behålla fungerande köksinredning och att pröva behovet av renovering. Arbetsversionen saknar färdigt rapportnummer/ISBN. Den är ett projektspecifikt underlag och kan inte ensam verifiera en generell nationell faktor.

Frivillig byggdelspost använder antal likvärdiga byggdelar, kg CO₂e/st vid utbyte, kg CO₂e/st för reparation, referensår och senare utbytesår. Källa och bekräftad avgränsning krävs när antal är större än noll. Faktorerna ska avse samma funktion och avgränsning. Användaren måste avskilja posten från aggregerade renoveringsfaktorer för att undvika dubbelräkning. Den är noll och inaktiv som standard.

E_ref_y = antal × EF_utbyte / 1000 i referensåret, annars noll.
E_alt_y = antal × EF_reparation / 1000 i referensåret + antal × EF_utbyte / 1000 i det senare utbytesåret.

I alternativet med inget bevarande används samma utbyte som i referensen. Modulen följer en första utbyteshändelse per alternativ med konstant utbytesfaktor, inte alla framtida cykler. Framtida dekarbonisering av just byggdelsfaktorn är inte införd. Årsredovisningen och periodsummeringen gör en uppskjutning synlig. Om samma nya byggdel köps inom perioden kan den kumulativa besparingen försvinna eller bli negativ när reparationen räknas med. Om bytet ligger efter 2050 är nyttan en undviken belastning inom perioden; utsläppen har inte permanent upphört.

CIRA-fallet, 30 köksinredningar exklusive vitvaror och endast materialproduktion:
| Alternativ | kg CO₂e för 30 kök | kg CO₂e/kök |
|---|---:|---:|
| Nya köksinredningar | 19 450 | 648,333… |
| Renoverade/bevarade köksinredningar | 900 | 30 |
| Skillnad | 18 550 | 618,333… |

Detta motsvarar 18,55 ton för projektet, cirka 95,4 % lägre materialproduktionspåverkan, inte en 95,4-procentig minskning av alla byggnadsutsläpp. Förinställningens år 2026 och 2051 är illustrativa modellval; CIRA-kalkylen styrker inte dessa tidpunkter eller resterande livslängd. Originalrapportens andra jämförelse, inklusive vissa vitvaror, har en annan avgränsning och införs inte med samma faktor.

Fallet kommer från Lysekil och är inte en observation av Malmö. Om ingen DeSO väljs fördelas demonstrationen efter ursprungsbeståndets BTA. Vid verklig användning anges berörd DeSO och inventerat antal. Flyttning till en ort ska inte blandas ihop med att studieunderlagets alla effekter har validerats på den orten.

## Källornas användning och kontroll
Referenserna nedan har kontrollerats mot bilagornas titelsidor, metod och relevanta tabeller/avsnitt eller mot publicerande organisation/förlag. Där direkt webbläsning stoppats redovisas det. Forskningsartiklarna verifierar metodval och vilka parametrar som behövs; de verifierar inte Malmös lokala antaganden. Kalkylen i CIRA har kontrollräknats, men inga nya mängdförteckningar eller EPD:er har tillförts. De ärvda verifieringsbehoven från 1.1 kvarstår.

### FISHMAN21
Fishman, T., Heeren, N., Pauliuk, S., Berrill, P., Tu, Q., Wolfram, P. och Hertwich, E.G. (2021). A comprehensive set of global scenarios of housing, mobility, and material efficiency for material cycles and energy systems modeling. Journal of Industrial Ecology, 25, 305–320.
Länk: https://doi.org/10.1111/jiec.13122
Kontroll: Bilagd PDF, figur 2 och scenariometod; titel, författare, år och DOI kontrollerade i artikeln.
Tillämpning och begränsning: Yta per person, beläggning, livslängd och materialeffektivitet behövs för scenarier. Inga globala mål översätts automatiskt till Malmö-BOA.

### ALAUX24A
Alaux, N., Schwark, B., Hörmann, M., Ruschi Mendes Saade, M. och Passer, A. (2024). Assessing the prospective environmental impacts and circularity potentials of building stocks: An open-source model from Austria (PULSE-AT). Journal of Industrial Ecology, 28, 1435–1448.
Länk: https://doi.org/10.1111/jiec.13558
Kontroll: Bilagd PDF, metod och tabell 1.
Tillämpning och begränsning: Koppling mellan byggnadsbestånd, area, energi och materialflöden. 44 mot cirka 55 m²/person och minskad vakans är österrikiska scenariovärden, inte effektfaktorer för Malmö. Scenariobakgrunderna skiljer sig också.

### ALAUX24B
Alaux, N., Obrecht, T.P., Saade, M.R.M. och Passer, A. (2024). A Need for Sufficiency in the Built Environment: Prospective Life Cycle Assessment of the Austrian Building Stock. IOP Conference Series: Earth and Environmental Science, 1363, 012002.
Länk: https://doi.org/10.1088/1755-1315/1363/1/012002
Kontroll: Bilagd PDF, avsnitt 2.4 och resultat.
Tillämpning och begränsning: 46 m²/person i utgångsläget, 55,3 i framskriven referens och 44 i WAM-SUF. Minskningen 55,3 till 44 är cirka 20 %, medan 46 till 44 är cirka 4 %. Resultatets procenttal får inte användas som generell svensk rabatt.

### NICK24
Nick, S. (2024). Systems perspectives on transforming Swiss housing by 2040: wellbeing, shared spaces, sufficiency, and de-sprawl. Frontiers in Sustainability, 5, 1375271.
Länk: https://doi.org/10.3389/frsus.2024.1375271
Kontroll: Bilagd PDF, avsnitt 2.2.3 samt diskussion om genomförande.
Tillämpning och begränsning: Normativt schweiziskt systemscenario. Privata, gemensamma och offentliga ytor har olika avgränsning; totalen 35 m²/person ska inte matas in som svensk BOA. Stöd för att redovisa boendekvalitet och service tillsammans med area.

### NESS22
Ness, D. (2022). Towards sufficiency and solidarity: COP27 implications for construction and property. Buildings and Cities, 3(1), 912–919.
Länk: https://doi.org/10.5334/bc.268
Kontroll: Bilagd PDF, policyanalys och slutsatser.
Tillämpning och begränsning: Stöd för behovsprövning, anpassning av befintligt bestånd och fördelningsfrågor. Ingen empirisk Malmöfaktor.

### NESS23
Ness, D.A. (2023). Technological efficiency limitations to climate mitigation: why sufficiency is necessary. Buildings and Cities, 4(1), 139–157.
Länk: https://doi.org/10.5334/bc.297
Kontroll: Bilagd PDF, syntes och slutsatser.
Tillämpning och begränsning: Stöd för att skilja absolut resursbehov från förbättrad klimatintensitet. Används inte som kvantitativ besparingskoefficient.

### HANSEN23
Hansen, R.N., Hoxha, E., Andersen, C.E., Rasmussen, F.N., Ryberg, M.W. och Birgisdottir, H. (2023). Closing the gap to sufficiency-based absolute climate targets for wood buildings. Journal of Physics: Conference Series, 2600, 182002.
Länk: https://doi.org/10.1088/1742-6596/2600/18/182002
Kontroll: Bilagd PDF, avsnitt 2.1–2.2, fyra fall och 50-årig funktionell enhet.
Tillämpning och begränsning: Stöd för att minskad byggd area och längre brukande behöver analyseras. Danska koldioxidbudgetar, 50-årsresultat och biogena slutskedeseffekter överförs inte till Malmös period 2025–2050.

### CIRA2
Sondal, J., Blixt, A.-M., Jonasson Tolv, J. och Vaara, E. (u.å.). Cirkulär och inkluderande renovering av allmännyttan – CIRA-processen 2.0. Användarlevererad arbetsversion.
Länk: Användarlevererad DOCX; ingen publik länk verifierad.
Kontroll: Bilagd DOCX, avsnitt om Lysekils kök och klimatberäkningar. Författare och siffror lästa i filen. Rapportnummer/ISBN är inte färdigställda.
Tillämpning och begränsning: 30 kök, köksinredning exklusive vitvaror: 19 450 kg vid nytt mot 900 kg vid renovering, endast materialproduktion. Kontrollräkning: 648,333 respektive 30 kg/kök; 18 550 kg = 18,55 ton skillnad. Ingen extern oberoende verifiering av kalkylunderlaget. Inga generella kg/m² härleds.

### EU24SUF
European Commission, Directorate-General for Environment, BPIE och Ramboll (2024). Sufficiency in the building sector: For the whole life carbon roadmap – final report. ISBN 978-92-68-20566-2.
Länk: https://op.europa.eu/en/publication-detail/-/publication/da276a27-b2b7-11ef-acb1-01aa75ed71a1/language-en
Kontroll: Utgivarmetadata kontrollerade via EU:s publikationssida, DOI 10.2779/5787055; direkt återöppning gav 429.
Tillämpning och begränsning: Kompletterande metodstöd för befintligt bestånd som alternativ till nybyggnad. Ingen faktor från ej fullständigt kontrollerad rapporttext införs.

### PAULIUK24
Pauliuk m.fl. (2024). Scenario analysis of supply- and demand-side solutions for circular economy and climate change mitigation in the global building sector. Journal of Industrial Ecology.
Länk: https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.13557
Kontroll: Förlagets originaltext: avsnitt 2.1 och tabell 1.
Tillämpning och begränsning: Service–bestånd–flöde kopplas samman. Regionala ytnivåer och långa livslängder är scenariodata, inte en generell besparing som ska multipliceras med Malmös total.

### GALIM24
Galimshina, A., Moustapha, M., Hollberg, A., Lasvaux, S., Sudret, B. och Habert, G. (2024). Strategies for robust renovation of residential buildings in Switzerland. Nature Communications, 15, 2227.
Länk: https://www.nature.com/articles/s41467-024-46305-9
Kontroll: Förlagets indexerade original och bibliografi kontrollerade; direkt återöppning stoppad av inloggningsomdirigering.
Tillämpning och begränsning: Byggskedets extra klimatpåverkan måste vägas mot driftbesparing. Ingen schweizisk isolerings- eller energifaktor används i modellen.

### SCBBOA24
SCB (2025). Hushållens boende 2024, statistiknyhet 24 april.
Länk: https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/bostader-och-boende/hushallens-boende/pong/statistiknyhet/hushallens-boende-2024/
Kontroll: Originalsidan kontrollerad: rikets genomsnittliga bostadsarea 42 m²/person.
Tillämpning och begränsning: Jämförelsevärde, inte observerad Malmöarea, miniminorm eller värde för en ny bostad. Statistikens area ska inte sammanblandas med Atemp eller BTA.

### WBCSD25AE
WBCSD (2025). Avoided Emissions in the Built Environment, 17 september.
Länk: https://www.wbcsd.org/resources/avoided-emissions-in-the-built-environment/
Kontroll: Utgivarens sektorsida och kopplingen till Guidance on Avoided Emissions v2.0 kontrollerade.
Tillämpning och begränsning: Metodstöd för en avgränsad jämförelse med referens. Modellen gör inte anspråk på certifiering, verifierade klimatkrediter eller full efterlevnad av vägledningen.


# Gemensam modellbeskrivning från 1.1 (cirkularitetsavsnitt ersätts av 1.2 ovan)

## Bedömning
Modellen är användbar för översiktlig klimatplanering, men kartans precision får inte förväxlas med säkra kausala effekter. Den viktigaste utvecklingen är att följa fysisk aktivitet (yta, kWh, fordonskm och kol) och göra skillnad mellan observerade data, skattningar, scenarier och belagda samband. Sociala, ekologiska och ekonomiska mål behöver egna indikatorer vid sidan av CO₂e.

## Förbättringar i denna version
- Befolkning 2030 rättad från 382 056 till 381 846 enligt Malmö stads tabell 1 (MALMO25). 2035 oförändrad. Långsiktig framskrivning bibehållen och märkt som modellval.
- Småhus klassas automatiskt med uppskattad Atemp. BTA 130 och Atemp/BTA 0,9 ger Atemp 117 och därmed den mindre kategorin (BOV26). Eget läge finns för annan metod.
- Energianvändning för faktiskt rivet ursprungligt bestånd dras av proportionellt. Ersättningsbyggnaders drift tillkommer. Renovering kan ges en egen energibesparing.
- Mark: valbar andel av kolförlust som räknas som utsläpp inom perioden. Förtätningens markanspråk begränsas till tillgänglig ohårdgjord areal med en försiktig reservation för utbyggnadsområden.
- Förtätning kan få egen extra anläggningsfaktor, utöver gemensam grundläggning. Default 0 är en datalucka.
- Mobilitet: explicit byte från biltrafik till alternativa färdsätt, med beläggning och alternativens klimatfaktor. Lokala basårsdata kan ersätta kommunproxyer per DeSO.
- Ny flik Stadsutveckling & indata, källkontroll och känslighetsanalys. Metodfliken beskriver även begränsningarna i den nya versionen.

## Vad hållbar stadsutveckling behöver beskriva
| Perspektiv | Klimatdrivare | Minsta indata | Fördjupat underlag | Genomförande 1.1 |
|---|---|---|---|---|
| Mark | Tidigare markanvändning, koltäthet, areal som förändras och kolöde | ha ohårdgjord mark, SOC/DOM/biomassa, exploaterad andel | jorddjup, schaktvolymer, massornas destination, oxidationsförlopp och referensscenario | förlustandel och arealbegränsning; schaktkedja ännu inte separat |
| Nyexploatering | Ytbehov, typologi, material och infrastruktur | invånare, hushåll, BTA per typ, byggår, A1–A5 och separata anläggningsposter | materialmängder, EPD, ledningslängder, gatuytor, geoteknik, byggtid | småhuskategori korrigerad; förtätningstillägg tillgängligt |
| Mobilitet | Närhet, funktionsblandning, kollektivtrafik och bilinnehav | fordon/hushåll, fordonskm/år, faktor per fordonskm | RVU-personkm per färdmedel, GTFS-turtäthet, faktisk gångtid, parkering och lokala mätningar | lokala bil- och km-data samt explicit färdmedelsbyte; ingen automatisk tillgänglighetselasticitet |
| Energi | Beståndets area, användning, renovering och energiförsörjning | Atemp, el och värme kWh/år, klimatfaktorer | byggnadsvisa tidsserier, väderkorrigering, timprofiler, effektbehov, lokal värmemix och marginalanalys | rivning/ersättning och renoveringsbesparing; ingen timmodell |
| Cirkularitet | Nyttjandegrad, återstående livslängd och ersatt funktion | omvandlingsbar BTA, påbyggnadspotential, renoverad BTA, faktorer och kapacitetstak | vakansgrad, bärighetsinventering, produktinventering, kvalitet och återbrukslogistik | cirkulära flöden och deras energi; återbruk ligger kvar som explicit antagande |

IPCC (2022), kapitel 8, ger stöd för att studera urban form och samordning mellan sektorer. Den kunskapen motiverar variabelvalen men ger inte automatiskt storleken på en Malmöeffekt. Tillgänglighetsindex ska därför användas som beskrivning eller kalibrerad förklaringsvariabel, inte som en otestad utsläppsrabatt.

## Beräkningskedja och enheter
Alla komponenter beräknas per kalenderår och DeSO, 2024–2050. 1 000 kg = 1 ton; 1 ha = 10 000 m². Basåret innehåller befintlig mobilitet och energi. A och B är alternativa transportperspektiv. Kontrollerna summerar DeSO till staden. Grunddata kommer från grund_deso.json, kol_deso.json, utbyggnad_op2023.json och geografilagren. Importen lokalaData ligger i scenariofilen och ersätter uttryckligen valda basårsvärden utan att skriva över grunddata.

### 1. Behov och geografisk fördelning
Nya invånare N=max(0, folkmängd_y−folkmängd_y−1). Negativ förändring påverkar områdesbefolkningen men frigör inte automatiskt bostäder eller tar bort trafik; detta är en kvarstående förenkling.
Bostäder=N×(1−andel i befintligt bestånd)/personer per bostad. Yta=bostäder×viktad BTA×(1−ytminskning). Lokaler=N×(arbetsplatser/inv×BTA/arbetsplats+skolyta/inv)×(1−minskning av lokalyta).
Omvandling och påbyggnad begränsas av respektive andel, kvarvarande kapacitetstak och flerbostadsbehov. Resten nybyggs. Ersättningsbyggande=rivningsavsikt×(1−renoveringsandel). Renoveringsandel avser alltså att undvika en rivning.
Bostäder fördelas till ÖP-områden efter kvarvarande bostadskapacitet, fokus eller modellens förenklade klimatpoäng. Resterande bostäder fördelas som förtätning. Lokaler fördelas efter arbetsplatser respektive befintlig yta. Årlig lokalyta har ännu inte ett fullt separat kapacitetstak per ÖP-område. Klimatordningen är inte en global optimering.

### 2. Mark
Potentiell kolförlust=tagen ohårdgjord ha×(1−ohårdgjord andel i slutläget)×[max(0,SOC+DOM−kvarvarande markkol)+biomassa]×44/12. Histogrammet summerar 10×10-metersrutor (0,01 ha). Årets förändring följer ökningen av exploaterad andel. Utsläpp inom perioden=potentiell förlust×vald andel/100; bokföring sker det år marken tas i anspråk. Detta är inte en fysisk nedbrytningskurva. Kvarvarande 22 t C/ha är inte lokalt verifierat (EJVER).
Förtätning begränsas till max(0, DeSO:s ohårdgjorda ha−reserverad ohårdgjord areal i utbyggnadsområden−redan använd förtätningsmark). Reservationen använder arealandelar, inte en ny geometrisk överlagring. Förrådslager är statiska basårsindikatorer och ska inte adderas till utsläpp. Framtida inlagring i träd, biokol och mark ingår inte i totalsumman.

### 3. Byggande och anläggning
Byggande=Σ BTA_typ×kg CO₂e/m² BTA_typ,år×materialscenario×återbruksscenario/1 000 + faktiskt riven BTA×rivningsfaktor/1 000. Småhus: Atemp≈BTA×(1−ytminskning)×Atemp/BTA. Automatiskt läge väljer 196/150 under 130 m² Atemp och 171/130 annars (referens/föreslaget 2030-värde). Egna småhusvärden används bara i eget läge.
Anläggning=[all nybyggd BTA inklusive ersättning×grundfaktor+utvecklad mark i ÖP-områden, m²×anläggningsfaktor+ny bostads-BTA vid förtätning×extra förtätningsfaktor]×index/1 000. Den extra faktorn kompletterar, inte ersätter, grundfaktorn. Grundförstärkning måste skiljas från byggdelar som redan ingår i byggnadsfaktorn (BOV26). Underhåll och utbyte av infrastruktur ingår inte som full livscykel.

### 4. Transport
Befintlig biltrafik=bränslekedja×flottindex+laddel×elindex+fordonstillverkning×tillverkningsindex. Årets trafikförändring multiplicerar summan. Byte från bil till andra färdsätt: E_efter=E_bil×(1−s)+fordonskm×s×beläggning×g CO₂e/personkm_alternativ/1 000 000. s ökar linjärt från 0 år 2024 till vald andel 2050. Faktoren för alternativet är konstant och ska anges av användaren med jämförbar systemgräns. 0 är ett avgränsat scenario, inte ett generellt LCA-värde för cykel.
Nya hushåll×bilar/hushåll×km/bil ger ny bilvolym; samma färdmedelsbyte och faktorlogik används. I A fördelas tillkommande aktivitet på den befintliga trafikens geografi och vald andel inom Malmö. Det är inte en ny trafikmodell. Lokala km och bilinnehav påverkar B och nytillkommande hushåll, men ersätter inte uppmätt trafik på A:s vägar. Fordonstillverkning minskar proportionellt med trafik i scenariot; detta är en aktivitetsallokering, inte omedelbar utskrotning. Rebound och inducerad trafik beräknas inte separat.

### 5. Energi och cirkularitet
Befintlig energi=[el kWh×el kg/kWh+värme kWh×värme kg/kWh]/1 000×generell effektivisering×beståndsfaktor. Beståndsfaktor=max(0,1−[ackumulerad faktiskt riven BTA+ackumulerad renoverad BTA×renoveringens besparing]/ursprunglig BTA). Rivna och renoverade andelar får inte tillsammans överstiga ursprungsbeståndet. Borttagen energi antas proportionell mot BTA. Modellen följer inte enskilda byggnader, så dessa två scenariobesparingar måste samordnas av användaren för att undvika överlappande åtgärdsmål.
Ny drift=ackumulerad nytillkommen Atemp inklusive ersättningsbyggnader och påbyggnad×kWh/m² Atemp×viktad klimatfaktor/1 000. Omvandlad lokalarea ligger redan i ursprungsbeståndet och läggs därför inte till igen. Ändrad energiprestanda efter omvandling är fortfarande en datalucka.
Cirkulärt byggskede=[omvandlad BTA×omvandlingsfaktor+påbyggd BTA×påbyggnadsfaktor×nybyggnadsfaktor+renoverad BTA×renoveringsfaktor]/1 000. Undvikna utsläpp är referensens byggande och mark minus alternativets byggande och mark. De dras inte av en gång till från totalen. Energi och transportskillnader ligger i sina respektive perspektiv. Kolförråd i träprodukter redovisas inte som verifierad permanent borttagning.

### 6. Tidsutveckling och resultat
En faktor hålls konstant till 2026, sedan multipliceras den för varje år med (1+r/100) för aktuell femårsperiod. Dessa takter är ärvda scenarier (EJVER). CCS är valfritt och avstängt; vald sänkning är en känslighetsparameter, inte verifierat lokalt utfall. Byggutsläpp bokförs vid färdigställande och full drift samma år, vilket överskattar driften för sent inflyttade etapper.
Årsresultat anges i t CO₂e/år, per ha land eller per invånare. Kumulativt resultat är summan 2025–2050. Divideras denna summa med slutårets invånare är det per invånare i slutåret, inte ett personårsgenomsnitt. Lokaliseringsindikatorn per bostad är en delindikator för byggande, mark och bilresor under en fast period; den omfattar inte hela modellens system och är inte en effektprognos av flytt.

## Källornas tillförlitlighet och kontroll
Två kontrollmoment betyder (1) utgivare, titel och version samt (2) stöd för det använda påståendet eller talet och dess avgränsning. Det är inte två oberoende studier. Status per källa framgår nedan och i fliken Källkontroll. Parametrar som inte har kunnat verifieras är tydligt märkta. Det vore fel att beteckna hela den ärvda parameteruppsättningen som dubbelverifierad.

### IPCC22: IPCC (2022). Climate Change 2022: Mitigation of Climate Change, kapitel 8, särskilt 8.4.2–8.4.4.
Status: Metodstöd kontrollerat.
Kontroll 1: IPCC:s publiceringssida och figur 8.21 identifierade.
Kontroll 2: Avsnittet anger täthet, funktionsblandning, gatunät och tillgänglighet som relevanta samband.
Begränsning: Ingen generell Malmöelasticitet eller automatisk procenteffekt härleds. Direkt öppning av kapitel/PDF gav 403; innehåll kontrollerat i indexerat original och figur.
Källa: https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-8/
Kompletterande länk: https://www.ipcc.ch/report/ar6/wg3/figures/chapter-8/figure-8-21/

### BOV26: Boverket (2026). Utkast färdplan för införande av gränsvärden för byggnaders klimatpåverkan. Rapport 2026:29.
Status: Identitet och tal kontrollerade.
Kontroll 1: Utgivarsida: titel, rapportnummer och utgivningsår.
Kontroll 2: Original-PDF: tabell 2, tryckt s. 33, och tabell 5, s. 43. Flerbostadshus 358/235, kontor 383/250. Småhus Atemp <130: 196/150, annars 171/130 kg CO2e/m² BTA.
Begränsning: Förslag, inte beslutad lag. Kontor används som proxy för samlad lokalyta. Atemp avgör småhuskategori, inte BTA. Alla grundläggningsposter får inte automatiskt adderas utan avgränsningskontroll.
Källa: https://www.boverket.se/sv/om-boverket/publikationer/2026/utkast-fardplan/
Kompletterande länk: https://www.boverket.se/globalassets/publikationer/dokument/2026/rapport-2026-29_utkast-fardplan-gransvarden-klimatpaverkan-byggnader.pdf

### ENERGI: Boverket (2026). Indata för energi.
Status: Tal och avgränsning kontrollerade.
Kontroll 1: Officiell handbok, avsnitt exempel på beräkning A5 energi.
Kontroll 2: Tabellens 0,037 kg CO2e/kWh el och 0,056 kg CO2e/kWh fjärrvärme kontrollerade, jämförda med klimatdatabasens metodsida.
Begränsning: Exemplet gäller byggplatsenergi. Här används faktorerna som redovisningsscenario även för drift. De är inte ett verifierat lokalt fjärrvärmevärde eller en marginalfaktor.
Källa: https://www.boverket.se/sv/klimatdeklaration/gor-sa-har/underlag/indata-om-energi/
Kompletterande länk: https://www.boverket.se/sv/klimatdeklaration/klimatdatabas/om-klimatdatabas/

### MALMO25: Malmö stad (2025). Bilagor till befolkningsprognos för Malmö 2025–2035, bilaga 1, tabell 1.
Status: Tabellvärden kontrollerade.
Kontroll 1: Kommunens beslutsunderlag och informationsartikel identifierade.
Kontroll 2: Tabell 1: 365644 år 2024, 381846 år 2030, 395094 år 2035. Tidigare interpolation 382056 ersatt.
Begränsning: Det är denna prognosversion som är kontrollerad, inte ett påstående om att den är senast publicerad. 2040–2050 är modellval. Mellan hållpunkter används linjär interpolation.
Källa: https://motenmedborgarportal.malmo.se/welcome-sv/namnder-styrelser/kommunstyrelsen/mote-2025-06-04/agenda/bilagor-till-befolkningsprognos-for-malmo-2025-2035pdf-11094?downloadMode=open
Kompletterande länk: https://malmo.se/Aktuellt/Artiklar-Malmo-stad/2025-06-04-Malmo-vaxer---men-i-langsammare-takt.html

### SLU25: SLU (2025). Maps: Carbon stock and carbon stock change in Swedish soils. Institutionen för mark och miljö.
Status: Metadata kontrollerade.
Kontroll 1: SLU:s officiella katalog: utgivare och dataset identifierade.
Kontroll 2: 10 × 10 m och separata lager för SOC och DOM samt förändring kontrollerade i lagerförteckningen.
Begränsning: De hämtade rastrens pixelvärden, djupdefinition och biomasstillhörighet har inte oberoende återvaliderats. Katalogen styrker inte att hela förlusten blir atmosfäriskt utsläpp direkt.
Källa: https://www.slu.se/en/environment/statistics-and-environmental-data/environmental-data-catalogue/maps-carbon-stock-and-carbon-stock-change-in-swedish-soils/
Kompletterande länk: 

### IVL22: IVL (2022). Vägledning ska minska klimatpåverkan vid renovering och ombyggnation, 7 december.
Status: Metodstöd kontrollerat, tal ej verifierade.
Kontroll 1: IVL:s originalpublicering bekräftar pilotprojekt och vägledning.
Kontroll 2: Publikationen bekräftar åtta fastighetsägare och behovet att väga byggskede mot drift; rapportlänk följs men DiVA gav botkontroll.
Begränsning: 40–160 och standard 100 kg/m² samt den gamla exakta författarhänvisningen är inte numeriskt verifierade här. Standard 100 behålls som scenarioantagande.
Källa: https://www.ivl.se/press/pressmeddelanden/2022-12-07-vagledning-ska-minska-klimatpaverkan-vid-renovering-och-ombyggnation.html
Kompletterande länk: https://ivl.diva-portal.org/smash/record.jsf?pid=diva2:1716345

### SCB25: SCB (2025). Geodata för DeSO – Demografiska statistikområden.
Status: Indelning identifierad.
Kontroll 1: Officiell geodatasida identifierad.
Kontroll 2: Versionsbyte till DeSO 2025 bekräftat i SCB:s information om indelningen.
Begränsning: Alla registeruttag i den ärvda datafilen har inte återhämtats och jämförts med SCB:s original. Kontrollsummor ger filintegritet, inte extern datavalidering.
Källa: https://www.scb.se/vara-tjanster/oppna-data/oppna-geodata/demografiska-statistikomraden-deso/
Kompletterande länk: https://www.scb.se/hitta-statistik/regional-statistik-och-kartor/regionala-indelningar/demografiska-statistikomraden-deso/

### ARVT: Road2Zero-OP, Vägvis 2.3.1 och Kolkarta Malmö (2026). Bifogade modellunderlag.
Status: Ärvt modellunderlag.
Kontroll 1: Kod, datafiler och medföljande dokumentation granskade lokalt.
Kontroll 2: Registersummeringar och beräkningsbalanser testade.
Begränsning: Alla mätningar, trafikfördelningar, energiskattningar och konfidensintervall har inte oberoende validerats. Dessa är en modellkedja, inte oberoende källor.
Källa: 
Kompletterande länk: 

### EJVER: Ärvda scenarioparametrar för framtida el, värme och fordonsflotta; kvarvarande markkol 22 t C/ha; grundläggning 26 kg/m²; anläggning 15 kg/m² mark.
Status: Numeriskt källstöd inte verifierat.
Kontroll 1: Värden och hänvisningar lokaliserade i den ursprungliga koden.
Kontroll 2: Sökning och avgränsningsgranskning ger inte tillräckligt stöd för exakt lokal tillämpning.
Begränsning: Behålls för versionsjämförelse som explicit antagande. IEA-, NV- och EU-etiketter är inte certifiering av dessa procentbanor. Återbruk 80 %, träfaktor 0,64, påbyggnad 0,7 och framtida CCS ingår i samma kontrollbehov.
Källa: 
Kompletterande länk: 

## Prioritering av fortsatt utveckling
1. Lokala mätningar av trafik och energianvändning, byggnadsbeståndets kvalitet och genomförbara omvandlingsytor.
2. Kalibrera resande mot RVU och använd nätbaserad tillgänglighet och GTFS som förklaringar. Skilj lokaliseringens effekt från hushållens självselektion, inkomst och livsfas.
3. Byt markschablon mot markövergångar och massbalans med dokumenterat kolöde. Lägg till referensscenario för framtida kolsänka först när underlag finns.
4. Geometri och verkliga mängder för gator, VA och grundförstärkning. Separata kapacitetstak för bostäder och lokaler.
5. Byggnadsvisa energikohorter, livslängd och återbruksmängder. Timvis effekt och lokal energidelning kräver en särskild energimodul.
6. Lägg till parallella indikatorer för boendekostnad, trångboddhet, serviceåtkomst, biologisk mångfald, värme- och översvämningsrisk. De ska inte omräknas till CO₂e utan belagd metod.

## Användning
Starta Streamlit med `streamlit run streamlit_app.py`, eller öppna den medföljande fristående HTML-filen. Inga GitHub Actions behövs. Befintliga scenario-JSON kan läsas in men resultat ändras av rättelserna; behåll gamla versionen för historiska jämförelser. I Stadsutveckling & indata kan lokala basårstal importeras som JSON med DeSO, år 2024 och källa. Tom mall fylls endast med verkliga värden. Importerade uppgifter är användaruppgifter, inte automatiskt verifierade data.

## Avgränsningskontroll för totalsumman
Laddel i trafikmodellen behöver stämmas av mot el som redan ingår i energistatistiken för byggnader. En elektrifierad fordonsflotta kräver även antaganden om laddvolymens utveckling. Denna version ärver en separat laddkomponent och beräknar inte dess fysiska volym ur en ny fullständig fordonsflotta. Därför är totalsumman ett screeningscenario, inte ett verifierat kommunalt växthusgasbokslut.

Byggdelsposten kräver separat aktivering efter kontroll av källa och avgränsning. CIRA-knappen fyller enbart indata och aktiverar inte posten i Malmötotalen. En demonstration är inte bekräftelse på att byggdelarna redan avskilts från andra klimatfaktorer.
