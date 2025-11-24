#!/usr/bin/env python3
# -*- coding: utf-8 -*-

translations = {
    # Komentáře v kódu
    "// Zavřít roletku při kliknutí mimo": "// Zamknij menu po kliknięciu poza nim",
    "// Spuštění animace při scrollu na graf": "// Uruchomienie animacji podczas przewijania do wykresu",
    "// Pro případ, že je graf už vidět při načtení": "// Na wypadek, gdy wykres jest już widoczny przy ładowaniu",
    "// Generujeme nebo získáme ID zákazníka při každém kliknutí": "// Generujemy lub pobieramy ID klienta przy każdym kliknięciu",
    "// Inicializujeme ID zákazníka hned při načtení stránky": "// Inicjalizujemy ID klienta natychmiast po załadowaniu strony",
    "// Validace jednotlivých polí při změně": "// Walidacja poszczególnych pól przy zmianie",
    "// Jazykový přepínač - roletka": "// Przełącznik języka - rozwijane menu",
    "// Zavřít roletku při kliknutí": "// Zamknij menu po kliknięciu",
}

def translate_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for cz, pl in translations.items():
        content = content.replace(cz, pl)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filename}")

translate_file("pl/index.html")
translate_file("pl/thank-you.html")


