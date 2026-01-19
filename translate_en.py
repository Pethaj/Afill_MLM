#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pro hromadný překlad zbývajících textů v EN index.html
"""

import re

# Slovník s překlady (česky -> anglicky)
translations = {
    # FAQ otázky
    "Je BEWIT multi-level marketing nebo pyramida?": "Is BEWIT multi-level marketing or a pyramid?",
    "Opravdu neplatím žádné poplatky?": "Do I really pay no fees?",
    "Musím plnit minimální obraty nebo prodávat určité množství?": "Do I have to meet minimum sales or sell a certain quantity?",
    "Musím mít živnostenský list?": "Do I need a business license?",
    "Kdy a jak mi budete posílat odměny?": "When and how will you send me rewards?",
    "Mohu pracovat odkudkoliv a nabízet produkty online?": "Can I work from anywhere and offer products online?",
    "Jakou podporu od vás dostanu?": "What support will I get from you?",
    
    # FAQ odpovědi
    "Ne, BEWIT není pyramida ani klasický MLM. Naše affiliate program je založený na doporučení produktů přes váš unikátní odkaz. Nejsou zde žádné vstupní poplatky, povinné balíčky ani nátlak na budování sítě. Zákazníci si sami vybírají, jak nakoupí – přes web, e-shop nebo přes vás. Provize dostanete vždy, ať už přivede prodej.": "No, BEWIT is not a pyramid or classic MLM. Our affiliate program is based on recommending products through your unique link. There are no entry fees, mandatory packages, or pressure to build a network. Customers choose how they shop – through the web, e-shop, or through you. You always get a commission, no matter how the sale comes in.",
    
    "Ano. Registrace i partnerský program jsou zcela zdarma. Neplatíte žádné vstupní poplatky, měsíční členství ani povinné nákupy. Získáte provizi z každého prodeje přes váš odkaz.": "Yes. Registration and the partner program are completely free. You pay no entry fees, monthly membership, or mandatory purchases. You get a commission on every sale through your link.",
    
    "Ne. U nás není žádný tlak na prodeje. Můžete sdílet produkty ve svém vlastním tempu, podle toho, jak vám to vyhovuje. Nemusíte plnit žádné minimální obraty.": "No. We have no pressure on sales. You can share products at your own pace, as it suits you. You don't have to meet any minimum sales targets.",
    
    "Pokud plánujete z příjmů z affiliate programu vytvořit si pravidelný zdroj příjmů, doporučujeme založit živnostenské oprávnění. Pro začátečníky a příležitostné doporučení to není nutné, ale záleží na vašich cílech a místních zákonech.": "If you plan to create a regular income from the affiliate program, we recommend establishing a business license. For beginners and occasional recommendations, it's not necessary, but it depends on your goals and local laws.",
    
    "Odměny vyplácíme měsíčně na základě vašich prodejů. Platbu obdržíte na bankovní účet, který uvedete při registraci. Vše sledujete transparentně v partnerské sekci.": "We pay out rewards monthly based on your sales. You'll receive payment to the bank account you provide during registration. You can track everything transparently in the partner section.",
    
    "Samozřejmě! Můžete pracovat odkudkoliv – z domu, z pláže nebo z kavárny. Potřebujete jen internet. K dispozici máte zdarma online marketingové nástroje, díky kterým můžete oslovit více lidí přes sociální sítě, blog nebo e-mail.": "Of course! You can work from anywhere – from home, the beach, or a café. All you need is internet. You have free online marketing tools that allow you to reach more people through social media, blog, or email.",
    
    "Získáte přístup do partnerské sekce s marketingovými materiály (bannery, fotky, texty). K dispozici jsou vám také online nástroje zdarma a naše partnerská podpora na telefonu a e-mailu, která vám ráda se vším pomůže.": "You'll get access to the partner section with marketing materials (banners, photos, texts). You also have free online tools and our partner support by phone and email, which will gladly help you with everything.",
    
    # JavaScript kalkulátor (v JS kódu)
    " Kč": " CZK",
}

def translate_file(filepath):
    """Přeloží texty v souboru"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Aplikuj překlady
    for czech, english in translations.items():
        content = content.replace(czech, english)
    
    # Pokud se něco změnilo, ulož
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Překlad dokončen: {filepath}")
        print(f"   Provedeno {len([k for k in translations if k in original_content])} změn")
    else:
        print(f"ℹ️  Žádné změny nebyly provedeny v: {filepath}")

if __name__ == "__main__":
    translate_file('/Users/petrhajduk/Documents/Code/Bewit/Affiliate_1/Afill_MLM/en/index.html')
