OpenCoden käytöönotto oli yksinkertaista. Käytin GPT 5 mini -mallia.

Metodin top_goal_scorers implementaatio ei noudattanut samaa tyyliä kuin mitä tiedostossa jo oli, mutta agentin tyyli oli "Python-maisempaa" kuin omani.

Koodin selittäminen vaikutti toimivan hyvin, ja agentti teki myös aikavaativuusanalyysin, kertoi minkälaiset inputit rikkovat metodin, miten tällaiset asiat voidaan korjata ja lopuksi vielä kertoi, mitä unittestejä pitää tehdä.

Agentti osasi selittää pylint-virheviestin ja bad-indentation-säännön olemassaolon syyn, mutta rehellisesti sanottuna asia oli aika ilmiselvä ihan kysymättäkin.

Uuden toiminnallisuuden tuottaminen ei toiminut suoraan, mutta kun pyysin agenttia korjaamaan virheet, sovellus alkoi toimia.

Myöskään testit eivät toimineet ensimmäisellä yrittämällä, vaan testitiedostoista puuttui importteja. Agentti kuitenkin pyydettäessä korjasi virheet, ja korjausten jälkeen testit toimivat.

Testit ovat eri näköisiä kuin käsin kirjoittamani testit viikolla 1. Stub luodaan kussakin testimetodissa ad hoc. Agentti myös kirjoitti assertit muotoa assert _totuusarvollinen lause_ sen sijaan, että olisi käyttänyt esim. assertAlmostEqual()-funktiokutsua.

Pylint ei löytänyt agentin koodista virheitä.

Olin positiivisesti yllättynyt siitä, että näinkin pieni ja vanha malli suoriutui näinkin hyvin, eikä esim. sotkenut mitään asiaankuulumatonta kohtaa missään tiedostossa. Agentin vastaukset tosin olivat hyvin pitkiä, ja tokeneita kului kokonaisuudessaan 61 % viikon saldosta.