#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oprava zbývajících českých textů a převod měny na PLN
"""

translations = {
    # České texty v index.html
    "Etické produkty so silným brandem": "Etyczne produkty z silną marką",
    "Objavuj, jak si vybudovať úspešný biznis s BEWITom – krok za krokom": "Odkryj, jak zbudować udany biznes z BEWIT – krok po kroku",
    "Stiahni si zadarmo e-book, v ktorom nájdeš krok za krokom vysvetlený systém, jak pracovať s BEWITom, získavať stabilný príjem a vybudovať si vlastnú rentu.": "Pobierz za darmo e-book, w którym znajdziesz wyjaśniony krok po kroku system, jak pracować z BEWIT, uzyskać stabilny dochód i zbudować własną rentę.",
    "Je BEWIT multi-level marketing alebo pyramída?": "Czy BEWIT to multi-level marketing lub piramida?",
    "Hlavné rozdiely oproti MLM:": "Główne różnice w porównaniu z MLM:",
    "Žiadne povinné nákupy ani vstupné balíčky": "Żadnych obowiązkowych zakupów ani pakietów startowych",
    "Férové ceny pre koncových zákazníkov": "Uczciwe ceny dla końcowych klientów",
    "Zarábate za skutočné predaje, nie za nábor ďalších predajcov": "Zarabiasz za rzeczywistą sprzedaż, nie za rekrutację kolejnych sprzedawców",
    "Akú podporu od vás dostanem?": "Jakie wsparcie od Was otrzymam?",
    
    # České texty v thank-you.html
    "Masz zájem o osobní setkání?": "Czy jesteś zainteresowany osobistym spotkaniem?",
    "Děkujeme za twój zájem!": "Dziękujemy za Twoje zainteresowanie!",
    "Dotazník byl úspěšně odeslán.": "Ankieta została pomyślnie wysłana.",
    "Brzy se vám ozveme s dalšími informacemi o affiliate programu.": "Wkrótce skontaktujemy się z Tobą z dodatkowymi informacjami o programie partnerskim.",
    
    # Měna - převod z EUR na PLN (přibližný kurz 1 EUR = 4.3 PLN)
    "92 €": "395 zł",
    "19 € za jeden": "82 zł za jeden",
    "20 €": "85 zł",
    "5 840 €": "25 110 zł",
    
    # Další možné výskyty
    "váš": "twój",
    "Váš": "Twój",
    "vám": "ci",
    "Vám": "Ci",
}

def translate_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for cz_text, pl_text in translations.items():
        content = content.replace(cz_text, pl_text)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filename}")

translate_file("pl/index.html")
translate_file("pl/thank-you.html")


