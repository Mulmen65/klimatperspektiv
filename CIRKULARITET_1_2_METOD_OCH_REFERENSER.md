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

Byggdelsposten kräver separat aktivering efter kontroll av källa och avgränsning. CIRA-knappen fyller enbart indata och aktiverar inte posten i Malmötotalen. En demonstration är inte bekräftelse på att byggdelarna redan avskilts från andra klimatfaktorer.
