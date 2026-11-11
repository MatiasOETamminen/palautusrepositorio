Minulla oli huomattavia vaikeuksia agentin kanssa tällä viikolla. Käytin edelleen GPT-5 mini -mallia OpenCoden läpi.

Pelkkä /init söi viikon tokeneista 63 %, ja lopputulos oli todella huono. Agentti ei missään vaiheessa ymmärtänyt, että riippuvuuksia hallitaan uv:lla, vaan olisi halunnut ohjeistaa itseään käyttämään pipiä. Oikean portin agentti kyllä löysi, mutta validaation sijainnin minun täytyi kirjoittaa käsin. Alkuperäinen AGENTS.md oli myös todella pitkä ja sisälsi täysin epärelevantteja asioita, joten pudotin suurimman osan sisällöstä pois.

Seuraava ongelma tuli, kun yritin pyytää agenttia kirjoittamaan testejä. Agentti ei löytänyt tiedostoa, vaikka osoitin sen sille @-syntaksilla. Kaikki tokenit se sen sijaan söi. Tässä kohdin pyysin tokenieni nollausta.

Kun tokenit oli nollattu, yritin uudelleen. Tällä kertaa agentti löysi osoitetun tiedoston (vaikken tehnyt mitään eri tavalla), ja totteli käskyä kirjoittaa testit ensin.

Kun pyysin agenttia sitten ajamaan testit, tämä ei onnistunut lainkaan, ja lupapyynnöt eri bash-komentojen ajoon alkoivat olla niin kryptisiä, että en antanut lupaa. En siis saanut agenttia missään vaiheessa ajamaan testejä itsenäisesti.

Varmistin sitten käsin, että testit todella failaavat, ja pyysin agenttia sitten toteuttamaan toiminnallisuudet. Agentti yritti jälleen kirjoitettuaan toteutuksen ajaa testit itsenäisesti, mutta se ei taaskaan onnistunut. Ajoin testit itse jälkikäteen, ja varmistin koodia tahallaan rikkoen, että ne todella toimivat (testit siis hajosivat odotetusti).

Positiivista oli se, että sekä agentin kirjoittamat testit että toteutukset toimivat heti halutulla tavalla.

Saman promptin ajaminen kahteen kertaan ja kahden eri tuloksen saaminen näytti konkreettisesti kielimallin ei-deterministisen luonteen.