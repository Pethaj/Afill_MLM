#!/usr/bin/env python3
# -*- coding: utf-8 -*-

translations = {
    "Zdieľajte informácie o kvalitných produktoch, ktoré sami používate a ktorým veríte – 100% prírodné, rastlinného pôvodu, bez chémie. Vďaka nášmu silnému brandu sa produkty predávajú ľahko, a to za konkurencieschopné ceny.": "Dziel się informacjami o wysokiej jakości produktach, których sam używasz i którym ufasz – 100% naturalne, pochodzenia roślinnego, bez chemii. Dzięki naszej silnej marce produkty sprzedają się łatwo, i to po konkurencyjnych cenach.",
    "Nasze korene sú v Beskydoch, náš dosah je celosvetový": "Nasze korzenie są w Beskidach, nasz zasięg jest globalny",
    "nielen Európa, ale aj trhy mimo nej.": "nie tylko Europa, ale także rynki poza nią.",
    "Systém odmien, ktorý má zmysel": "System prowizji, który ma sens",
    "Začni budovať svoj úspešný biznis s BEWIT – registruj sa ešte dnes a získaj e-book zadarmo, ktorý ti ukáže konkrétne kroky.": "Zacznij budować swój udany biznes z BEWIT – zarejestruj się już dziś i otrzymaj darmowy e-book, który pokaże Ci konkretne kroki.",
    "Nie, nie sme MLM ani pyramída.": "Nie, nie jesteśmy MLM ani piramidą.",
    "BEWIT je klasický affiliate program s jednoduchým princípom: zarábate províziu za predaje, ktoré prídu vďaka vašim odporúčaniam. Nevyžadujeme žiadne vstupné balíčky, nákupné povinnosti ani budovanie zložitých štruktúr pod sebou.": "BEWIT to klasyczny program partnerski z prostą zasadą: zarabiasz prowizję od sprzedaży, które pochodzą dzięki Twoim rekomendacjom. Nie wymagamy żadnych pakietów startowych, obowiązków zakupowych ani budowania skomplikowanych struktur pod sobą.",
    "Náš model je transparentný a férový – pomáhame vám zarábať odporúčaním kvalitných produktov, ktoré masz radi.": "Nasz model jest przejrzysty i uczciwy – pomagamy Ci zarabiać poprzez polecanie wysokiej jakości produktów, które kochasz.",
    "Získate prístup do partnerskej sekcie s marketingovými materiálmi (bannery, fotky, texty). K dispozícii sú vám aj online nástroje zadarmo a naša partnerská podpora na telefóne a e-maile, ktorá vám rada so všetkým pomôže.": "Otrzymasz dostęp do sekcji partnerskiej z materiałami marketingowymi (bannery, zdjęcia, teksty). Masz również do dyspozycji darmowe narzędzia online oraz naszą pomoc partnerską telefonicznie i przez e-mail, która chętnie pomoże we wszystkim.",
    
    # Opravy částečně přeložených vět
    "Dziel się informacjami o wysokiej jakości produktach, których sam używasz i którym ufasz": "Dziel się informacjami o wysokiej jakości produktach, których sam używasz i którym ufasz",
    "ktorý ti ukáže": "który pokaże Ci",
    "ktoré prídu vďaka vašim odporúčaniam": "które pochodzą dzięki Twoim rekomendacjom",
    "ktoré masz radi": "które kochasz",
    "ktorá vám rada so všetkým pomôže": "która chętnie pomoże we wszystkim",
}

def translate_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for sk, pl in translations.items():
        content = content.replace(sk, pl)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filename}")

translate_file("pl/index.html")
translate_file("pl/thank-you.html")



