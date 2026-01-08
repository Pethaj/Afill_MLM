#!/usr/bin/env python3
# -*- coding: utf-8 -*-

translations = {
    # Zbývající slovenské fráze
    "Bez nátlaku, bez minimálnych obratov, bez skladovania. Len vy, vaše odporúčanie a provízie až 30 % z každého predaja.": "Bez presji, bez minimalnych obrotów, bez magazynowania. Tylko Ty, Twoja rekomendacja i prowizje do 30% od każdej sprzedaży.",
    "Z každého predaja cez váš unikátny odkaz": "Z każdej sprzedaży przez Twój unikalny link",
    "získavate až 30%": "otrzymujesz do 30%",
    "Priemerná hodnota objednávky našich zákazníkov je 92 €.": "Średnia wartość zamówienia naszych klientów to 92 €.",
    "Zaujímavé odmeny od výrobcu pri zachovaní konkurencieschopných cien.": "Atrakcyjne prowizje od producenta przy zachowaniu konkurencyjnych cen.",
    "Navštívte našu firmu, prejdite si výrobu a získajte dôveru pre vaše odporúčanie. Silný brand uľahčuje rozširovanie siete.": "Odwiedź naszą firmę, zobacz produkcję i zbuduj zaufanie dla swojej rekomendacji. Silna marka ułatwia rozwijanie sieci.",
    "Ako rastie váš pasívny príjem s Bewit": "Jak rośnie Twój pasywny dochód z Bewit",
    "Když se vaše doporučení šíří dál – přátelé vašich zákazníků nakoupí – systém vás odmění automaticky.": "Kiedy Twoja rekomendacja rozprzestrzenia się dalej – przyjaciele Twoich klientów kupią – system automatycznie Cię nagrodzi.",
    
    # Další možné výrazy
    "váš": "twój",
    "Váš": "Twój",
    "vaše": "twoje",
    "Vaše": "Twoje",
    "našich": "naszych",
    "Našich": "Naszych",
    "naše": "nasze",
    "Naše": "Nasze",
    "našu": "naszą",
    "Našu": "Naszą",
    "Ako ": "Jak ",
    "ako ": "jak ",
    "Kedy ": "Kiedy ",
    "kedy ": "kiedy ",
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



