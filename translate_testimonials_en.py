#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pro překlad testimonials v EN index.html
"""

# Slovník s překlady testimonials (české → anglické)
translations = {
    # Testimonial 1 - Vlada Pipková
    '"Nádherná citrusová vůně jako kdybych rozkrojila čerstvě utržený, chemicky neošetřený, pomeranč. V mžiku navodí pozitivní náladu a energii, voní dětem i dospělým. Tento olejíček je u nás doma velmi oblíbený. Využíváme ho často i v kuchyni."':
    '"Beautiful citrus scent as if I had cut open a freshly picked, chemically untreated orange. It instantly creates a positive mood and energy, loved by children and adults alike. This oil is very popular in our home. We often use it in the kitchen too."',
    
    'Pomeranč esenciální olej': 'Orange Essential Oil',
    
    # Testimonial 2 - Petra Kubánková
    '"Jsem milovníkem kávy a tak se stala Coffee king mým ranním rituálem. Káva plné a silné chuti, kterou si připravuji obvykle s Bio Organic Coconut milk powder. Společně s houbičkami vzniká naprosto bezkonkurenční koktejl chutí. Tahle káva předčila mé očekávání."':
    '"I am a coffee lover and Coffee King has become my morning ritual. A full-bodied and strong-flavored coffee that I usually prepare with Bio Organic Coconut milk powder. Together with the mushrooms, it creates an absolutely unbeatable cocktail of flavors. This coffee exceeded my expectations."',
    
    # Testimonial 3 - Martin N.
    '"Tenhle olejíček je další můj favorit na první dobrou, jak se říká. Nejenže krásně voní, je to další produkt, který mi nesmí chybět jak doma, tak v práci, na cestách, v autě. Vždy je mi nápomocen, takový anděl strážný. Když ho mám jsem v klidu, každá situace vždy dobře dopadne."':
    '"This oil is another instant favorite of mine, as they say. Not only does it smell beautiful, it\'s another product that I can\'t be without at home, at work, on the road, or in the car. It always helps me, like a guardian angel. When I have it, I\'m at peace, every situation always turns out well."',
    
    'Soulguard esenciální olej': 'Soulguard Essential Oil',
    
    # Testimonial 4 - Lada J.
    '"Nevím proč, ale vůně mi lehce připomíná vůni lineckého cukroví. Tyto oleje Suby C-1,2,3 si mě k sobě přivolaly, já jim otevřela své srdce a pustila je dovnitř. Tak nějak po nich vnitřně volám, aby svou laskavostí naplnily mé zmatené buňky a opravily jim špatnou mapu."':
    '"I don\'t know why, but the scent slightly reminds me of the smell of Linzer cookies. These Suby C-1,2,3 oils called me to them, I opened my heart to them and let them in. I somehow call to them internally to fill my confused cells with their kindness and fix their faulty map."',
    
    'Suby C-3 esenciální olej': 'Suby C-3 Essential Oil',
    
    # Testimonial 5 - Michaela Salsová
    '"Skořice Kasie to byla láska hned na první nadechnutí. Velmi příjemná vůně… jako by byla smíchána i se skořicí. Koupila jsem na zkoušku malou lahvičku, ale hned jdu objednat dvě velké. Na podzim a v zimě se bude velmi hodit."':
    '"Cassia Cinnamon was love at first breath. Very pleasant scent... as if it was mixed with cinnamon. I bought a small bottle to try, but I\'m going right now to order two large ones. It will be very useful in autumn and winter."',
    
    'Skořice Kasie esenciální olej': 'Cassia Cinnamon Essential Oil',
}

def translate_file(filepath):
    """Přeloží testimonials v souboru"""
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
        print(f"✅ Testimonials přeloženy: {filepath}")
        print(f"   Provedeno {len([k for k in translations if k in original_content])} změn")
    else:
        print(f"ℹ️  Žádné změny nebyly provedeny v: {filepath}")

if __name__ == "__main__":
    translate_file('/Users/petrhajduk/Documents/Code/Bewit/Affiliate_1/Afill_MLM/en/index.html')
