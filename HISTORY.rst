]

==============
Historia zmian
==============

202101.55
---------

* opcjonalnie pokazuj autorów zerowych w raporcie slotów-uczelnia (#941),
* optymalizacja algorytmu liczącego dla zadania dużej ilości slotów w sytuacji,
  gdy pracownik jej nie osiąga (b/n).

202101.54
---------
* poprawne wyświetlanie charakteru formalnego dla doktoratów i habilitacji
  w widoku prac (b/n),
* możliwość wyszukania prac z ustawioną strona WWW [errata] (#865),
* aktualizacja pakietu django-password-policies-iplweb do wersji 0.8.0 (b/n),
* aktualizacja pakietu django-multiseek do wersji 0.9.43 (b/n),
* lepsze wyszukiwanie wg daty utworzenia rekordu dla zakresu dat (#932),
* wyświetlaj link do PubMedCentral dla prac z PMC ID (#959),
* poprawki pobierania PubMed ID (#958),
* poprawne zawężanie do zakresu punktów PK (#967),
* katalog cache ma nazwę z numerem wersji (#961),
* raport slotów uczelnia wg algorytmu plecakowego (#923),
* w multiwyszukiwarce w polu "Wydawnictwo nadrzędne" pokazuj wyłącznie rekordy
  będące już wydawnictwami nadrzędnymi dla rekordów (#953).

202101.53
---------
* poprawne opisy powiązań autora z dyscypliną w module redagowania (#686)
* zezwalaj na więcej, niż jedną pracę doktorską dla autora (#873)
* pełne BPP ID na stronie pracy (#951)
* możliwość wyszukania prac z ustawionym DOI (#864)
* możliwość wyszukania prac z ustawioną strona WWW (#865)
* opcjonalnie traktuj jako slot zerowy prace z PK=5 (#877)
* wygodny podgląd powiązań autora z dyscypliną w module redagowania (b/n)
* możliwość eksportu danych dyscyplin autorów w formacie XLS (#893)
* wyświetlanie rekordów powiązanych dla wydawnictw zwartych (#897)
* wyszukiwanie rekordów powiązanych dla wydawnictw zwartych (#897)

202101.52
---------
* raport slotów - autor umożliwia zbieranie "do N slotów" dla autora (b/n),
* konfigurowane wartości domyślne dla daty w formularzach (#947)
* wyszukiwanie pełnotekstowe uwzględnia myślniki (#851)
* poprawne wyszukiwanie po polu "Licencja OpenAccess ustawiona" (#934)
* możliwość wyszukiwania po polu "charakter formalny ogólny" (#933)
* poprawne wyszukiwanie w polach numerycznych (#913)
* możliwość powiązania zewnętrznej bazy danych również dla wydawnictwo zwartych (#935)
* poprawne działanie funkcjo restartującej hasło na produkcji (#936)

202012.51
---------
* zbieranie slotów dla autora za pomocą algorytmu plecakowego (b/n),
* ukrywanie statusów korekt w multiwyszukiwarce (#942),
* ukrywanie statusów korekt przy obliczaniu slotów -
  liczenie punktów za sloty w zależności od ustawienia statusu korekty (#945),
* ukrywanie wybranych statusów korekt w rankingach (#946),
* ukrywanie wybranych statusów korekt w raortach (#943),
* ukrywanie wybranych statusów korekt w API (#946),

202011.50
---------
* prawidłowe obliczanie punktów dla tłumaczeń (#931)

202011.49
---------
* podczas obliczania slotów dla liczby autorów z dyscypliny nie uwzględniaj autorów
  z odznaczonym polem "afiliuje" (#927)
* pole "pseudonim" dla autora (#921)
* wyświetlanie wewnętrznego ID autora na podstronie autora (b/n),
* możliwość otwarcia strony autora po ID za pomocą linku /bpp/autor/{ID}/ (b/n),
* prawidłowe obliczanie punktów dla referatów (#930)

202009.48
---------
* umożliwiaj konfigurację domyślnych wartości parametrów dla
  wybranych formularzy oraz wyświetlanie dowolnego tekstu HTML przed i
  po formularzach (#922)
* zamiast zbierać prace na minimalny slot, zbieraj prace do osiągnięcia maksymalnego
  slotu: usunięta zostaje opcja "minimalny slot" oraz "wyświetlaj prace poniżej minimalnego
  slotu", dodana zostaje opcja "maksymalny slot" (#917)
* licz sloty dla roku 2021 jak dla roku 2020 (#925)
* poprawka błędu edycji wydawców (#925)

202008.47
---------

* ograniczaj wyświetlanie do 20 tys rekordów przy braku zapytania w wyszukiwarce (b/n),

202008.46
---------

* możliwość przypisywania grantów rekordom (b/n),
* możliwość przypisywania elementów repozytoryjnych (plików) rekordom (b/n),

202008.45
---------

* backend cache zmieniony na django-redis-cache (wcześniej: pylibmc) (b/n),

202008.43
---------

* lepszy silnik notyfikacji dynamicznych (channels+ASGI+uvicorn) (b/n),
* import danych o dyscyplinach autorów z plików DBF (b/n),
* dodatkowe pola "rodzaj autora" oraz "wymiar etatu" (b/n),
* import danych grantów, nr odbitek i liczne drobne poprawki importu DBF (b/n),

202007.41
---------

* poprawione regenerowanie opisów bibliograficznych (#875)
* prawidłowe renumerowanie kolejności z poziomu polecenia nawet w sytuacji gdy afiliacja
  autora przypisana jest niepoprawnie (afiliuj="tak" przy obcej jednostce) (b/d)
* prawidłowe wyszukiwanie wydawnictw nadrzędnych w module redagowania (#882)

202006.40
---------

* poprawne importowanie niektórych akcentowanych znaków z plików DBF (n/d),
* zamień pola "szczegóły" i "informacje" przy imporcie (#857)
* opcjonalna walidacja pola "Afiliowana" przy przypisaniu autora do rekordu
  za pomocą zmiennych środowiskowych (n/d),
* dodatkowe pole "nie eksportuj do API" dla rekordów wydawnictw zwartych, ciągłych,
  patentów, prac doktorskich i habilitacyjnych.

202006.39
---------

* prace habilitacyjne i patenty w API (#859)
* nie importuj pola źródła 200C w przypadku importu DBF dla prac z redaktorami (#797)
* przy imporcie z plików DBF ustawiaj to samo ID jednostki co po stronie DBF (n/d)
* przy imporcie plików DBF poprawnie importuj wartości niepoprawnie zapisane w DBF (#876)
* upoważnienie PBN - pole (#840)

202006.38
---------

* procedura serwerowa do wycinania wartości pola ISBN z pola "Uwagi" (#796)
* poprawione wycinanie numerów i suplementów (#845)
* lepszy opis dla rekordów z wydawnictwem nadrzędnym - oznaczenie wydania dla rozdziałów (#843)
* charakter formalny dostaje nowe pole - charakter ogólny (książka/rozdział/artykuł) (wynika z #843)
* wyświetlaj informacje o czasie udostępnienia OpenAccess w API (#861)

202005.37
---------

* eksport promotora w pracach doktorskich w API (b/n),
* pole "oznaczenie wydania" (#843),
* poprawnie importuj ilość stron dla monografii dla plików DBF (#847),
* lepsze przypisywanie grup punktowych w imporcie DBF (b/n),

202005.36
---------

* poprawki importu rekordów z plików DBF oraz procedur wycinających
  dane na temat numeru i tomu (#845)
* import z plików DBF zachowuje oryginalne numery ID (b/n),
* eksport prac doktorskich w API (b/n),

202004.35
---------

* filtrowanie po roku publikacji w API (#844)

202004.34
---------

* zmiany nazw kolumn raportu ewaluacji (#830)
* dodatkowe pola metryczki rekordu oraz sumowanie w XLS w raportach slotów
  (#829),
* rozszerzanie listy źródeł przy imporcie plików DBF (b/n),
* nie wymagaj wydziału przy eksporcie do PBN - eksportuj całą uczelnię (#828)
* wygodniejsze sortowanie wydziałów w module redagowania oraz możliwość
  ręcznego sortowania jednostek (#802)

202004.33
---------

* eksport pola public-uri do PBNu eksportuje w pierwszej kolejnosci adres publiczny,
  w drugiej - płatny, adresy generowane na podstawie PubMedID nie są już wysyłane (#834)
* eksportowane jest pole book-with-chapters do PBN (#824)
* nie usuwaj spacji przed kropką przy imporcie publikacji (b/n),

202004.32
---------

* filtrowanie po charakterze formalnym w API (b/n)

202004.31
---------

* filtrowanie po dacie w REST API dla obiektów Autor,
  Wydawnictwo_Ciagle, Wydawnictwo_Zwarte, Zrodlo (b/n),
* dodatkowe pola ISSN / EISSN w REST API (b/n),
* eksportuj identyfikator ORCID autora do PBN, datę modyfikacji rekordu
  dla wydawnictw, datę dostępu dla OpenAccess (#824)

202003.29
---------

* Django 3.0 (b/n),
* REST API (b/n),
* narzędzie do dzielenia "podwójnych" wydawców po imporcie (b/n)

202003.27
---------

* napraw błąd importu pliku dyscyplin uniemożliwiający zmianę zaimportowanych już
  dyscyplin (b/n),
* drobne poprawki zachowania admina (nie wyświetlaj listy tabel z importem danych z
  pliku DBF jeżeli nie są zaimportowane, nie pozwalaj na usuwanie własnego konta,
  nie pozwalaj na usunięcie ostatniego konta superużytkownika, nie wyświetlaj
  komunikatu błędu gdy próbujemy dopisać rekord z powiązaniem autora do rekordu
  w sytuacji gdy nie podano jednostki) (b/n),

202003.26
---------

* wyświetlaj również wydawnictwa zwarte w raporcie slotów - ewaluacja (b/n),
* skracaj listę autorów gdy powyżej 100 znaków dla widoku HTML w raporcie slotów - ewaluacja (b/n),
* umożliwiaj filtrowanie raportu slotów - ewaluacja (b/n),

202003.25
---------

* wyświetlaj kolumnę z ilością wszystkich autorów w raporcie slotów - autor (#807)
* wyświetlaj mniejsze czcionki w raporcie slotów - autor
* raport slotów - ewaluacja (#809)

202003.23
---------

* wyświetlaj dodatkowe kolumny w raporcie slotów - autor (#807)

202003.22
---------

* regresja: błędy raportu slotów (#811)

202003.21
---------

* regresja: wyszukuj po polu "Dostęp dnia (wolny dostęp)" (#815)
* regresja: wyszukuj prawidłowo prace w obcych jednostkach (#816) + poprawki
  wydajności,
* ustalaj obcą jednostkę w uczelni przy imporcie (b/d),
* nie pozwalaj na ustalenie nie-obcej jednostki jako obcej dla uczelni (b/d),
* regresja: wyszukuj prawidłowo prace w obcych jednostkach (#816)
* poprawnie wyszukuj przypisania autora do dyscypliny w multiwyszukiwarce (b/d),
* mniejsza ilość zapytań o grupy użytkownika w redagowaniu (b/d),

202003.20
---------

* ORCID i PBN ID w raport slotów - uczelnia (#808),
* wyświetlanie numeru PBN ID na stronie autora (b/n),
* licz sloty tylko dla autorów afiliowanych (#810)
* w przypadku zaznaczenia opcji 'afiliuje' przy obcej jednostce, zgłaszaj błąd (b/n),
* operatory do multiwyszukiwarki: afiliuje TAK/NIE, dyscyplina ustawiona TAK/NIE,
  obca jednostka TAK/NIE (umożliwia zapytania z #816, #817, #814, #815)

202003.19
---------

* import pliku DBF nie dzieli tytułu po znaku równości na oryginalny i pozostały (b/n),
* autorom przypisanym do rekordów patentów można przypisywać dyscypliny naukowe (b/n),
* aktualizacja pakietów zależnych z przyczyn bezpieczeństwa (bleach3) (b/n),
* eksport PBN: eksportuj prace z PK większym, niż 5 (poprzedni warunek: większe lub równe) (b/n),
* aliasy wydawców (b/n),
* tworzenie źródła wprost z formularza dodawania wydawnictwa ciągłego w module redagowania (#800),
  tak utworzone źródło dostanie zawsze rodzaj źródła równy: periodyk,
* wyświetlanie PubMed ID, PMC ID oraz ISBN i ISSN w opisie bibliograficznym (#801, #799),

202002.18
---------

* wyświetlaj lata dla raportu zerowego w jednej kolumnie (#812)
* nie uwzględniaj wpisów dyscyplin bez punktacji w raporcie zerowym (#785)
* umożliwiaj oddzielne zarządzanie widocznością raportu slotów zerowych (#785)
* nie dodawaj pola 103 do konferencji przy imporcie DBF (#794)
* akceptuj podwójnych autorów przy imporcie DBF (#792)
* poprawnie rozpoznawaj formę główną autora (#806)
* poprawnie importuj z plików DBF numery stron i pola szczegółów (#795, #796)

202002.17
---------

* umożliwiaj poprawne wylogowanie użytkownika z systemu, bez wyświetlania strony błędu (#714)
* nie zgłaszaj awarii dla eksportu XLS pustych skoroszytów dla raportu slotów - autor (#782)
* umożliwiaj poprawne resetowanie hasła użytkownika (#675)
* napraw błąd w wyszukiwaniu pełnotekstowym (#683)

v202002.16
----------

* raport slotów "zerowy", pokazujący autorów z zadeklarowaną dyscypliną, ale bez prac w tej
  dyscyplinie (#785)

v202002.15
----------

* rezygnacja z Pipfile na rzecz pip-tools
* rezygnacja z Raven na rzecz sentry-sdk
* zmiany eksportu do PBN:

  * wyrzucono pole eksport-pbn-size,
  * wyrzucono pole employed-in-unit dla autorów/redaktorów,
  * wykasowano pola "other-contributors", generują się wszyscy autorzy (również obcy)
  * dla książek pod redakcją generują się wszyscy redaktorzy oraz nie generują się autorzy rozdziałów
  * dla książek i rozdziałów generują się tylko publikacje z punktacją PK>5

v202001.14
----------

* poprawiony błąd związany z obliczaniem punktów dla dyscyplin z dziedziny nauk humanistycznych, etc.
  (sentry:BPP-UP-8Q)

v202001.12
----------

* poprawne obliczanie punktacji dla dyscyplin z dziedziny nauk humanistycznych, społecznych i teologicznych (#775)
* mniejszy rozmiar pliku wynikowego (whl)
* usunięto minimalną ilośc slotów dla raportu slotów - uczelnia (#781)
* rozbijanie raportu slotów - uczelnia na jednostki i wydziały (#784)

v201911.9
---------

* import baz danych z systemów zewnętrznych
* równolegle działające polecenie rebuild_cache, przyspieszające czas nocnej przebudowy cache bazy

v201910.7
---------

* niezwykle eleganckie tabele w XLS wraz z opisem (#766)
* bardziej widoczny indeks wydawców w module redagowania (#771)
* uwzględniaj prace posiadające 100 punktów PK dla "Monografia – wydawnictwo poziom I" (#770)
* klikalny tytuł pracy w raporcie slotów (#772)
* raport slotów z możliwością podania parametru poszukiwanej ilości slotów i opcjonalnym
  wyświetlaniem autorów poniżej zadanego slotu (#765)
* nie licz slotów dla prac wieloośrodkowych (typ KBN=PW) (#761)
* zmiana nazwy kolumny "PKdAut" na "punkty dla autora" (#754)
* wyświetlaj punkty PK w raporcie autora (#769)
* nie kopiuj linku do płatnego dostępu w opcji "tamże" (#722)
* konfigurowalne "Rozbij punktację na jednostki" dla rankingu autorów (#750)

v201910.6
---------

* możliwość niezależnego ustalenia opcji widoku raportów "raport slotów - uczelnia" i "raport slotów - autor"
* poprawne kasowanie wcześniej zapisanej informacji o slotach i punktach
* poprawki pobierania arkuszy XLS dla raportu slotow - poprawnie eksportowane liczby, szerokośc kolumn

v201910.5a0
-----------

* raport slotów - uczelnia: eksport do XLS bez tagów HTML, możliwość filtrowania
* usunięto zdublowaną tabelę dla raportu slotów autorów

v201910.1a0
-----------

* tabelki z możliwością eksportu XLS - punkty i sloty dla autorów i uczelni

v201909.0001-alpha
------------------

* przełączenie na system wersji numerowanych od kalendarza (calver, #746)

* opcje wyświetlania raportu slotów i tabelki z punktacją slotów na podstronie pracy -- dla wszystkich,
  tylko dla zalogowanych lub dla nikogo.

* nie licz slotów dla punkty PK = 0 dla wydawnictw ciągłych

* możliwość umieszczenia dowolnego tekstu przed i po liście autorów w opisie bibliograficznym

1.0.31
------

* drobne poprawki zmiany nazwy raportu slotów

1.0.31-dev3
-------------

* w przypadku braku wpisanej wartości w pole "liczba znakow wydawniczych", do paczek dla PBN
  wrzucaj wartosc 0 (zero). Pole wg Bibliotekarzy nie jest już wymagane przez Ministerstwo,
  zas oprogramowanie PBN na ten moment jeszcze tego pola wymaga.

* kolumna z PK dla raportu slotów

* poprawiono matchowanie autorów dla importu dyscyplin w sytuacji szukania autora po tytule
  naukowym (#742)

1.0.31-dev2
-------------

* polecenie do automatycznego przypisywania dyscyplin - dla autorów, którzy mają przypisaną tylko
  jedną dyscyplinę dla danego roku, można za pomocą polecenia command-line przypisać z automatu
  tą dyscyplinę do wszystkich ich prac, które nie mają przypisanej dyscypliny

* raport slotów

1.0.31-dev1
-------------

* nie wymagaj ilości znaków wydawniczych od rozdziałów i monografii przy eksporcie dla PBN

* połącz 3 pola obiektu Charakter Formalny: "Artykuł w PBN", "Rozdział w PBN", "Ksiażka w PBN" w jedno
  pole "Rodzaj dla PBN", które to może przyjąć jedną z 3 powyższych wartości; wcześniejszy model umożliwiał
  eksportowanie jednego charkateru formalnego jako rozdział bądź książka, jednakże po usunięciu
  warunku dotyczącego liczby znaków wydawniczych, niektóre rekordy mogłyby w takiej sytuacji być
  eksportowane więcej, niż jeden raz.

* konfigurowalne podpowiadanie dyscypliny autora (w sytuacji gdy ma tylko jedną na dany rok) podczas
  przypisywania autora do rekordu publikacji; zmiana konfiguracji za pomoca obiektu 'Uczelnia' (#728),

* poprawka błędu gdzie dla autorow z dwoma dyscyplinami była podpowiedź dyscypliny a nie powinno jej byc
  (#729)

* rozbicie pliku test_admin.py na klika mniejszych celem usprawnienia efektywności testow uruchamianych
  za pomocą pytest-xdist (na wielu procesorach)


1.0.31-dev0
-------------

* liczenie punktów i slotów dla wydawnictw zwartych

* "charakter dla slotów" dla charakteru formalnego

* informacja o możliwości (lub niemożliwości) policzenia punktów dyscyplin dla rekordu w panelu administracyjnym

1.0.30-dev3
-------------

* "rozbieżności dyscyplin" - moduł umożliwiający podejrzenie różnic pomiędzy dyscyplinami
  przypisanymi na dany rok dla autora a dyscyplinami przypisanymi do rekordów

* lepsza obsługa kolejki cache

1.0.30-dev2
-------------

* poprawki drobnych błędów

1.0.30-dev1
-------------

* drobne poprawki

1.0.30-dev0
-------------

* poprawki

1.0.29-dev3
-------------

* wyświetlanie informacji o punktacji dla dyscyplin i slotach

1.0.29-dev2
-----------

* powiązanie rekordu publikacji z autorem pozwala również wprowadzić informację
  na temat dyscypliny

1.0.29-dev1
-----------

* umożliwiaj konfigurację opcji "pokazuj liczbę cytowań na stronie autora",

* poprawione kasowanie patentów

* poprawne wyszukiwanie po dyscyplinach

* procent odpowiedzialności za powstanie pracy wyświetla się na podstronie pracy


1.0.28
------

* poprawki importu dyscyplin: lepsze dopasowywanie autora z jednostką z pliku wejściowego
  do danych w systemie

* poprawiony błąd importu dyscyplin utrudniający poprawne wprowadzenie pliku do bazy

* możliwość wyszukiwania przez ORCID w multiwyszukiwarce oraz w globalnym wyszukiwaniu

* numer ORCID staje się unikalny dla autora


1.0.27
------

* dyscyplina główna i subdyscyplina wraz z procentowym udziałem

* możliwość identyfikowania autorów po ORCID przy imporcie dyscyplin

* nowy plik z przykładowymi informacjami dla importu dyscyplin,

* możliwość przypisywania rodzaju kolumny przy imporcie dyscyplin,

* możliwosć wprowadzania procentowego udziału odpowiedzialności autora w powstaniu
  publikacji

* Django 2.1

1.0.26
------

* wyszukiwanie zaawansowane: gdy podane jest imię i nazwisko ORAZ np jednostka lub
  typ autora, wyniki będą poprawne tzn związane ze sobą (autor + afiliacja), a nie
  tak jak do tej pory pochodzące z dowolnych powiązań autora do rekordu,

* nowy operator dla pól autor, jednostka, wydział, typ odpowiedzialności "równy+wspólny",
  który zachowuje się tak, jak do tej pory zachowywał się operator "równy". Gdy chcemy
  znaleźć rekordy wspólne opublikowane przez dwóch lub więcej autorów/jednostki/wydziały,
  gdy chcemy znaleźć rekordy, które np. mają typ autora "redaktor" i "tłumacz" - korzystamy
  z tego operatora; gdy chcemy znaleźć prace autora afiliowane na konkretną jednostkę,
  korzystamy z operatora "równy"

* kosmetyka wyświetlania szczegółów rekordu: pole "Zewnętrzna baza danych", justowanie
  nagłówków do prawej strony.

* wyszukiwanie: prawidłowo obsługuj zapytania o rekordy zarejestrowane
  w kilku zewnętrznych bazach danych

1.0.27-alpha
------------------------------

* obsługa punktacji SNIP

1.0.25
------

* mniejsza wielkość tytułu na wydruku z opcji "Wyszukiwanie" (#632)

* tytuł naukowy autora nie wchodzi do elementu opisu bibliograficznego rekordu
  (#633)

* możliwość określania drzewiastej struktury dla charakterów formalnych - określanie
  charakterów nadrzędnych, wraz z możliwością wyszukiwania z uwwzględnieniem
  tej struktury (#630)

* możliwość określenia dla rankingu autorów, aby wybierane były jedynie prace
  afiliowane na jednostkę uczelni (= czyli taką, która ma zaznaczone "skupia
  pracowników" w module Redagowanie - Struktura) (#584)

1.0.23
------

* możliwość skonfigurowania, czy na wydrukach z "Wyszukiwania" ma pojawiać się logo
  i nazwa uczelni oraz parametry zapytania (#603)

* poprawki wydruków - mniejsza czcionka i marginesy (#619)

* ukryj liczbę cytowań dla użytkowników niezalogowanych w wyszukiwaniu; dodaj raporty
  z opcjonalnie widoczną liczbą cytowań (#626)

* pozwalaj na określanie szerokości logo na wydrukach przez edycję obiektu "Uczelnia"

* automatycznie dodawaj ciąg znaków "W: " dla opisu bibliograficznego wydawnictwa
  zwartego (#618)

* wyszukiwanie po liczbie autorów, możliwość wyszukiwania rekordów bez uzupełnionych
  autorów (#598)

* możliwość sortowania przy użyciu pól liczba autorów, liczba cytowań, data ostatniej
  zmiany, data utworzenia rekordu i innych (#589)

* kropka na końcu opisu bibliograficznego, prócz rekordów z DOI (#604)

* definiowana ilość rekordów przy której pojawia się opcja "drukuj" i "pokaż wszystkie"
  dla użytkowników zalogowanych i anonimowych, poprzez edycję obiektu Uczelnia (#610)

* możliwość podglądania do 100 rekordów wydawnictw zwartych i ciągłych powiązanych
  do konferencji

* możliwość jednoczasowej edycji do 100 rekordów powiązań autora i jednostki w module
  redagowanie, przy edycji obiektu Jednostka

1.0.21
------

* możliwość ustalenia domyślnej wartości pola "Afiliuje" dla rekordów wiążących
  rekord pracy z rekordem autora

* możliwość wyszukiwania po liczbie cytowań; wyświetlanie liczby cytowań w tabelkach
  wyszukiwania

* możliwość pokazywania liczby cytowań w rankingu autorów z opcjonalnym ukrywaniem
  tego parametru za pomocą modułu redagowania (opcje obiektu Uczelnia)

* możliwość pokazywania liczby cytowań na podstronie autora z opcjonalnym ukrywaniem
  tego parametru za pomocą modułu redagowania (opcje obiektu Uczelnia)

* poprawiono błąd powodujący niewłaściwe generowanie eksportów PBN dla rekordów książek
  w których skład wchodziło powyżej 1 rozdziału (#623)

* poprawne wyświetlanie raportów jednostek i wydziałów, zgodne z ustawieniami
  obiektu "Uczelnia"

* poprawne eksportowanie do PBN konferencji indeksowanych w WOS/Scopus (#621)

* poprawione generowanie plików XLS w niektórych środowiskach (#601)

* możliwość określania rodzaju konferencji w module redagowanie: lokalna, krajowa,
  międzynarodowa oraz wyszukiwania po typach konferencji (#620)

1.0.20
------

* możliwość wyszukiwania nazwiska autora dla pozycji 1-3, 1-5 oraz dla ostatniej
  pozycji - dla użytkowników zalogowanych

1.0.19
------

* możliwość globalnej konfiguracji sposobu wprowadzania powiązań autorów z rekordami

1.0.18
-------

* obsługa API WOS-AMR od Clarivate Analytics

* lepsze wyświetlanie rekordu patentu w widoku rekordu

* poprawka formularza edycji autorów powiązanych z rekordem w module redagowania -
  obecnie edycja odbywa się za pomocą formularzy poziomych, co zwiększyło czytelnosć

* możliwość oznaczania i wyszukiwania rekordów indeksowanych w zewnętrznych bazach danych
  (np. WoS, Scopus) dla wydawnictw ciągłych

* nazwa konferencji zawiera etykietę "WoS" lub "Scopus" w przypadku, gdy konferencja
  jest indeksowana,

* eksport PBN działa poprawnie w przypadku podania tej samej daty w polu "od" i "do"

* ukrywanie pól w "wyszukiwaniu" oraz brak dostępu do raportów zgodnie z ustawieniami
  systemu dokonanymi w module "Redagowanie"

1.0.17
------

* import i wyszukiwanie dyscyplin naukowych

1.0.16 (2018-03-20)
-------------------

* błąd wyświetlania strony w przeglądarce Edge został naprawiony,

* data ostatniej modyfikacji dla PBN wyświetla się dla zalogowanych użytkowników

1.0.15 (2018-03-07)
-------------------

* dodatkowe pole dla typu odpowiedzialności, umożliwiające mapowanie charakterów
  formalnych autorów na charaktery formalne dla PBN

* nowe pola dla patentów: wydział, rodzaj prawa patentowego, data zgłoszenia,
  numer zgłoszenia, data decyzji, numer prawa wyłącznego, wdrożenie.

* impact factor dla Komisji Centralnej ma 3 pola po przecinku (poprzednio 2)

* zmiana sposobu nawigacji na menu na górze ekranu,

* wyszukiwanie zyskuje nową szatę graficzną i animacje.

1.0.4 (2018-02-13)
------------------

* poprawienie błędu wyszukiwania autorów w przypadku, gdy w wyszukiwanym
  ciągu znajdzie się spacja,

* zezwalaj na dowolną wartość zapisanego imienia i nazwiska w module
  redagowania,

* umożliwiaj wyszukiwanie po pierwszym nazwisku i imieniu (pierwszy autor,
  redaktor, etc)

1.0.1 (2018-01-01)
------------------

* wyświetlanie danych OpenAccess na widoku pracy,

* wyświetlanie DOI w opisach bibliograficznych, raportach oraz widoku pracy,

* poprawiony błąd budowania zapytania SQL na potrzeby wyszukiwania pełnotekstowego

0.11.112 (2017-12-09)
---------------------

* wyszukiwanie konferencji w globalnej nawigacji modułu redagowania

0.11.111 (2017-11-16)
---------------------

* poprawiony błąd związany z wyborem pola "tylko prace z afiliowanych jednostek"
  występujący w formularzu raportu autorów

* optymalizacja wyświetlania podstrony jednostki w przypadku, gdy zawiera
  ona więcej, niż 100 autorów.

0.11.109 (2017-11-14)
---------------------

* możliwość przejścia do panelu redagowania z każdej strony serwisu, gdzie
  tylko ma to sens (jednostki, autorzy, artykuły, wydziały),

* kosmetyczne poprawki wyświetla raportów,

* poprawiony błędny warunek dla funkcji raportu autorów "uwzględniaj tylko
  prace afiliowanych jednostek uczelni",


0.11.107 (2017-11-12)
---------------------

* opcja "Stwórz autora" tworzy domyślnie autora niewidocznego na stronach
  jednostek, kapitalizując nazwiska,

* poprawiono błąd powodujący niepoprawne działanie funkcji usuwania
  pojedynczych rekordów z wyników wyszukiwania.

0.11.106 (2017-11-10)
---------------------

* możliwość łatwego przechodzenia z formularza edycji w module redagowania do
  stron WWW dostepnych dla użytkownika końcowego

* [kod] generowanie opisu bibliograficznego autorów za pomocą systemu
  templatek Django; usunięcie kodu generowania opisu bibliograficznego
  autorów za pomocą własnych tagów,

* pole "Pokazuj na stronach jednostek" dla Autorów staje się polem "Pokazuj"
  i określa widoczność autora na stronie jednostki oraz w "Rankingu autorów"


0.11.104 (2017-11-08)
---------------------

* usunięto błąd uniemożliwiający edycję już zapisanego autora w rekordach
  wydawnictwa ciągłego i zwartego

0.11.103 (2017-11-06)
---------------------

* od tej wersji, dla wydawnictw zwartych, gdzie określone jest wydawnictwo nadrzędne,
  nie ma już potrzeby uzupełniania pola "Informacje", gdyż system w opisie
  bibliograficznym użyje tytułu wydawnictwa nadrzędnego,

* miniblog - możliwość umieszczenia aktualności na pierwszej stronie serwisu.

* obsługa przycisku "Uzupełnij rok" dla wydawnictwa zwartego (uzupełnia dane
  na podstawie pola "Szczegóły" bądź z "Wydawnictwo nadrzędne") oraz dla
  wydawnictwa ciągłego (uzupełnia dane na podstawie pola "Informacje").

0.11.101 (2017-11-03)
---------------------

* opcjonalne uwzględnianie prac spoza jednostek uczelni w raportach autorów,

* naprawiono działanie konektora OAI-PMH,

* "prawdziwa" funkcja "pozostałe prace" dla raportów,

* poprawione wyświetlanie rekordów (poprawna obsługa tagów "sup" i "sub"
  w opisach bibliograficznych).


0.11.90 (2017-09-23)
--------------------

* opcjonalne rozbicie na jednostki i wydziały w rankingu autorów

* możliwość ukrycia pola "Praca recenzowana"

* poprawki wyświetlania podstron autora i jednostki

0.11.77 (2017-09-19)
--------------------

* poprawiono liczenie punktacji sumarycznej w rankingu autorów

* poprawiono wyszukiwanie dla podanych jednocześnie par autor + jednostka

* poprawki wydajności wyszukiwania

0.11.55 (2017-08-30)
--------------------

* domyślne sortowanie rankingu autorów

* obsługa PostgreSQL 9.6

0.11.53 (2017-08-29)
--------------------

* poprawiony błąd eksportowania plików XLS i DOCX utrudniający ich otwieranie

* poprawiony błąd wyszukiwania dla pola "Źródło"

* opcjonalne ukrywanie elementów menu serwisu dla użytkowników zalogowanych
  i niezalogowanych


0.11.50 (2017-08-23)
--------------------

* poprawiony błąd uniemożliwiający sortowanie w rankingu autorów

* tabela rankingu autorów stylizowana podobnie jak inne tabele w systemie

* możliwość eksportowania rankingu autorów oraz raportów autorów, jednostek i
  wydziałów w różnych formatach wyjściowych (m.in. MS Excel, MS Word, CSV)


0.11.43 (2017-08-15)
--------------------

* możliwość zmiany wyglądu kolorystycznego systemu

* nowy framework raportów oparty o zapytania w języku DSL, obsługiwany
  w pełni przez użytkownika końcowego

* konfigurowalny czas długości trwania sesji - możliwość wybrania, jak długo
  system czeka na reakcję użytkownika przed automatycznym jego wylogowaniem

* autorzy przy wyszukiwaniu przez globalną nawigację oraz w module "Redagowanie"
  wyświetlani są zgodnie z ilością publikacji w bazie

* możliwość automatycznego utworzenia autora i serii wydawniczej
  podczas wpisywania rekordu - bez konieczności przechodzenia do innej częsci
  modułu redagowania

* opcja resetu hasła w przypadku jego zapomnienia

* konfigurowalny czas do przymusowej zmiany hasła, konfigurowalny moduł
  zapamiętujący ostatnio wpisane hasła oraz konfigurowalna ilość
  ostatnio zapamiętanych haseł

0.11.19 (2017-07-15)
--------------------

* do rekordu powiązania autora z wydawnictwem (zwartym, ciągłym lub patentem)
  dochodzi pole "afiliowany", domyślnie mające wartość 'PRAWDA'. Należy je
  odznaczyć w sytuacji, gdyby autor danej publikacji zgłosił powiązanie
  do jednostki będącej w strukturach uczelni w której jest zatrudniony jednakże
  jednoczasowo do tej publikacji zgłosił inną jednost

* do rekordu wydawnictwa zwartego, ciągłego, patentu, pracy doktorskiej i
  pracy habilitacyjnej dochodzą pola "strony", "tom" i "numer zeszytu":
  - w sytuacji, gdy są wypełnione, to ich wartości są używane do eksportu PBN,
  - w sytuacji, gdy są niewypełnione, system spróbuje wyekstrahować te dane z
    pól "szczegóły" i "informacje" analizując ciągi znaków, poszukując ciągów
    takich jak "vol.", "t.", "r.", "bd." dla tomu, "nr", "z.", "h." dla numeru
    zeszytu, "ss." lub "s." dla stron, "b. pag." dla braku paginacji,
  - podczas edycji rekordu w module "redagowanie" pola te zostaną uzupełnione
    przez system na podstawie pól "szczegóły" i "informacje" gdy użytkownik
    kliknie odpowiedni przycisk; w takiej sytuacji pola te, jeżeli zawierają
    jakieś informacje, zostaną nadpisane.

* konferencje - w module redagowania można dopisywać dane o konferencjach, które
  następnie mogą być przypisane do wydawnictwa ciągłego lub wydawnictwa
  zwartego

* struktura - w module redagowania za pomocą rekordu uczelni można ukryć
  wyświetlanie punktacji wewnętrznej oraz Index Copernicus

* autor - nowe pole "Open Researcher and Contributor ID"

* wygodna edycja kolejności wydziałów w module Redagowanie➡Struktura➡Uczelnia

* poprawiono błąd związany z obsługą pola dla rekordu Autor "Pokazuj na stronie
  jednostki". Autorzy którzy mają to pole odznaczone, nie będą prezentowani
  na stronach jednostek.

* dla typów KBN można określać odpowiadający im charakter PBN. Pole to zostanie
  użyte jako fallback w sytuacji, gdy rekord charakteru formalnego do którego
  przypisana jest dana praca nie ma określonego odpowiadającego mu charakteru
  PBN

* podgląd na znajdujące się w bazie charaktery PBN i przypisane im charaktery
  formalne i typy KBN w module "Redagowanie"

* w bloku "Adnotacje" w module "Redagowanie" wyświetla się ID oraz PBN ID

* pola "Seria wydawnicza" oraz "ISSN" dla wydawnictwa zwartego

* możliwość określania nagród oraz statusu wybitności pracy dla rekordów
  wydawnictw zwartych i wydawnictw ciągłych

* możliwość filtrowania po statusach openaccess w module "Wyszukiwanie" dla
  użytkowników niezalogowanych

0.11.0 (2017-07-05)
-------------------

* obsługa Python 3 + Django 1.10

0.10.96 (2017-04-02)
--------------------

* pierwsza publicznie dostępna wersja
