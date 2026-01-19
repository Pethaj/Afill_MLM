#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro překlad anglické verze do němčiny (DE)
"""

import re
import html

# Překlady z angličtiny do němčiny - pouze viditelné texty, formální vykání
translations = {
    # Meta tagy a titulky
    "Become a BEWIT Partner | Passive Income with Commission up to 30%": "Werden Sie BEWIT-Partner | Passives Einkommen mit bis zu 30% Provision",
    "Join the BEWIT affiliate program. Passive income without investment, without obligations. Commission up to 30% on every sale.": "Treten Sie dem BEWIT-Partnerprogramm bei. Passives Einkommen ohne Investition, ohne Verpflichtungen. Bis zu 30% Provision auf jeden Verkauf.",
    
    # Hero sekce
    "AFFILIATE PROGRAM": "PARTNERPROGRAMM",
    "BECOME A BEWIT PARTNER": "WERDEN SIE BEWIT-PARTNER",
    "Passive Income Without Obligations": "Passives Einkommen ohne Verpflichtungen",
    "Earn with products that make sense": "Verdienen Sie mit Produkten, die Sinn machen",
    "No pressure, no minimum sales, no storage. Just you, your recommendations, and commissions up to 30% on every sale.": "Kein Druck, keine Mindestumsätze, keine Lagerhaltung. Nur Sie, Ihre Empfehlungen und bis zu 30% Provision auf jeden Verkauf.",
    "Average reward: £16 per purchase.": "Durchschnittliche Belohnung: 16 £ pro Einkauf.",
    "Get Your Partner Link": "Holen Sie sich Ihren Partner-Link",
    "Share BEWIT products with family, friends, or on social media – and earn a commission on every sale. No obligations, no risks, no investment.": "Teilen Sie BEWIT-Produkte mit Familie, Freunden oder in sozialen Medien – und verdienen Sie bei jedem Verkauf eine Provision. Keine Verpflichtungen, keine Risiken, keine Investition.",
    "Join the Program For Free": "Kostenlos dem Programm beitreten",
    
    # O nás a výhody
    "Why Choose BEWIT?": "Warum BEWIT wählen?",
    "No Initial Investment": "Keine Anfangsinvestition",
    "You don't need to invest your own money or buy packages. Start earning right away, without risk.": "Sie müssen kein eigenes Geld investieren oder Pakete kaufen. Beginnen Sie sofort zu verdienen, ohne Risiko.",
    "No Purchase Obligations": "Keine Kaufverpflichtungen",
    "No pressure – you don't have to sell a minimum quantity of products or meet sales targets.": "Kein Druck – Sie müssen keine Mindestmenge an Produkten verkaufen oder Verkaufsziele erreichen.",
    "Work from Anywhere": "Arbeiten Sie von überall",
    "From home, the beach, or a café – all you need is internet. Online tools are free.": "Von zu Hause, vom Strand oder aus einem Café – alles, was Sie brauchen, ist Internet. Online-Tools sind kostenlos.",
    "Ethical Products with a Strong Brand": "Ethische Produkte mit einer starken Marke",
    "Share information about quality products you use and trust – 100% natural, plant-based, chemical-free. Thanks to our strong brand, products sell easily at competitive prices.": "Teilen Sie Informationen über Qualitätsprodukte, die Sie verwenden und denen Sie vertrauen – 100% natürlich, pflanzlich, chemiefrei. Dank unserer starken Marke verkaufen sich die Produkte leicht zu wettbewerbsfähigen Preisen.",
    "Our roots are in the Beskydy Mountains, our reach is global": "Unsere Wurzeln liegen in den Beskiden, unsere Reichweite ist global",
    "Join the BEWIT Community": "Treten Sie der BEWIT-Community bei",
    "BEWIT ✦ NO PRESSURE ✦ NO OBLIGATIONS ✦ JUST FAIR REWARDS ✦": "BEWIT ✦ KEIN DRUCK ✦ KEINE VERPFLICHTUNGEN ✦ NUR FAIRE BELOHNUNGEN ✦",
    "Over 15 Years on the Market": "Über 15 Jahre auf dem Markt",
    "We produce exclusive aromatherapy products with worldwide success.": "Wir produzieren exklusive Aromatherapie-Produkte mit weltweitem Erfolg.",
    "Wide Assortment and Loyal Customers": "Breites Sortiment und treue Kunden",
    "From essential oils to supplements – products customers love to come back to.": "Von ätherischen Ölen bis zu Nahrungsergänzungsmitteln – Produkte, zu denen Kunden gerne zurückkommen.",
    "High-Quality Products": "Hochwertige Produkte",
    "Pure, certified, and effective – no compromises.": "Rein, zertifiziert und wirksam – keine Kompromisse.",
    "Professional Marketing Materials": "Professionelle Marketingmaterialien",
    "We provide you with banners, texts, product descriptions, and everything you need.": "Wir stellen Ihnen Banner, Texte, Produktbeschreibungen und alles zur Verfügung, was Sie benötigen.",
    
    # Odměny a jak to funguje
    "How to Get Rewards?": "Wie erhalten Sie Belohnungen?",
    "A Reward System that Makes Sense": "Ein Belohnungssystem, das Sinn macht",
    "From every sale through your unique link, you earn up to 30%. The average order value of our customers is £77. Attractive rewards from the manufacturer while maintaining competitive prices.": "Bei jedem Verkauf über Ihren einzigartigen Link verdienen Sie bis zu 30%. Der durchschnittliche Bestellwert unserer Kunden beträgt 77 £. Attraktive Belohnungen vom Hersteller bei gleichzeitiger Aufrechterhaltung wettbewerbsfähiger Preise.",
    "You Don't Have to Worry About Anything": "Sie müssen sich um nichts kümmern",
    "We handle orders, payments, shipping, and customer support for you. You don't need a physical store or your own warehouse.": "Wir kümmern uns um Bestellungen, Zahlungen, Versand und Kundensupport für Sie. Sie benötigen kein physisches Geschäft oder eigenes Lager.",
    "Free Online Marketing": "Kostenloses Online-Marketing",
    "You have free access to online marketing tools, graphics, and support from our team. Reach more people online.": "Sie haben kostenlosen Zugang zu Online-Marketing-Tools, Grafiken und Unterstützung von unserem Team. Erreichen Sie mehr Menschen online.",
    "Strong Brand Helps Growth": "Starke Marke hilft beim Wachstum",
    "Visit our company, tour the production facility, and gain confidence for your recommendations. A strong brand makes network expansion easier.": "Besuchen Sie unser Unternehmen, besichtigen Sie die Produktionsanlage und gewinnen Sie Vertrauen für Ihre Empfehlungen. Eine starke Marke erleichtert die Netzwerkerweiterung.",
    "It doesn't matter which sales channel the customer chooses. The commission is always yours.": "Es spielt keine Rolle, welchen Verkaufskanal der Kunde wählt. Die Provision gehört immer Ihnen.",
    "Start Earning": "Beginnen Sie zu verdienen",
    "Your content, your networks, your reward.": "Ihr Inhalt, Ihre Netzwerke, Ihre Belohnung.",
    "How Your Passive Income Grows with BEWIT": "Wie Ihr passives Einkommen mit BEWIT wächst",
    "commission on every sale": "Provision auf jeden Verkauf",
    "From the 1st sale, you earn up to 30% commission. The more you sell, the higher your passive income.": "Ab dem ersten Verkauf verdienen Sie bis zu 30% Provision. Je mehr Sie verkaufen, desto höher ist Ihr passives Einkommen.",
    "1. Sign Up": "1. Registrieren Sie sich",
    "Quick registration – email and basic info.": "Schnelle Registrierung – E-Mail und grundlegende Informationen.",
    "2. Get Your Unique Link": "2. Erhalten Sie Ihren einzigartigen Link",
    "You'll receive your own affiliate link and a welcome package with marketing materials.": "Sie erhalten Ihren eigenen Affiliate-Link und ein Willkommenspaket mit Marketingmaterialien.",
    "3. Share and Earn": "3. Teilen und verdienen",
    "Share your link via social media, websites, blogs, or directly with friends.": "Teilen Sie Ihren Link über soziale Medien, Websites, Blogs oder direkt mit Freunden.",
    "Commission from the 1st sale, forever.": "Provision ab dem ersten Verkauf, für immer.",
    "Partnership with BEWIT – Different from Others": "Partnerschaft mit BEWIT – Anders als andere",
    "We Invite You for Coffee!": "Wir laden Sie zum Kaffee ein!",
    "When You Combine Authenticity with Quality": "Wenn Sie Authentizität mit Qualität verbinden",
    "Fair Approach. Real Results.": "Fairer Ansatz. Echte Ergebnisse.",
    "Do Business Without Borders": "Geschäfte ohne Grenzen machen",
    "Why BEWIT is Different:": "Warum BEWIT anders ist:",
    "Start Building Your Successful Business with BEWIT – Register Today and Get a Free E-book That Shows You the Specific Steps.": "Beginnen Sie mit dem Aufbau Ihres erfolgreichen Geschäfts mit BEWIT – Registrieren Sie sich heute und erhalten Sie ein kostenloses E-Book, das Ihnen die konkreten Schritte zeigt.",
    "Have Questions? We Have Answers.": "Haben Sie Fragen? Wir haben Antworten.",
    
    # Partnerství není MLM
    "No Starter Packages:": "Keine Starterpakete:",
    "You don't have to buy products you don't need. You can start completely free.": "Sie müssen keine Produkte kaufen, die Sie nicht brauchen. Sie können völlig kostenlos beginnen.",
    "No Pressure on Sales:": "Kein Verkaufsdruck:",
    "We don't require minimum sales. Offer only what you want, when you want.": "Wir verlangen keine Mindestumsätze. Bieten Sie nur an, was Sie wollen, wann Sie wollen.",
    "Fair Prices for Customers:": "Faire Preise für Kunden:",
    "– Attractive rewards at competitive prices.": "– Attraktive Belohnungen zu wettbewerbsfähigen Preisen.",
    "We're Not a Pyramid or MLM:": "Wir sind keine Pyramide oder MLM:",
    "You earn directly from your recommendations, not from building complex structures.": "Sie verdienen direkt aus Ihren Empfehlungen, nicht aus dem Aufbau komplexer Strukturen.",
    "Global Potential:": "Globales Potenzial:",
    "Strong brand with worldwide reach – not just Europe, but markets beyond.": "Starke Marke mit weltweiter Reichweite – nicht nur Europa, sondern Märkte darüber hinaus.",
    "Quality and Community:": "Qualität und Gemeinschaft:",
    "Our products spread easily. Thanks to quality, experiences, and a community of people who love them. Share your story – the system does the rest for you.": "Unsere Produkte verbreiten sich leicht. Dank Qualität, Erfahrungen und einer Gemeinschaft von Menschen, die sie lieben. Teilen Sie Ihre Geschichte – das System erledigt den Rest für Sie.",
    "Fair Partnership": "Faire Partnerschaft",
    
    # Coffee invitation
    "We'd love to welcome you personally and show you behind the scenes at BEWIT – from production and research to our shipping warehouse. This way, you'll get an authentic idea of what you're promoting. And if you want, you can immediately shoot your first reels video, which will give your followers inspiration directly from where it happens.": "Wir würden Sie gerne persönlich willkommen heißen und Ihnen einen Blick hinter die Kulissen von BEWIT zeigen – von der Produktion und Forschung bis zum Versandlager. So erhalten Sie eine authentische Vorstellung davon, was Sie bewerben. Und wenn Sie möchten, können Sie sofort Ihr erstes Reels-Video drehen, das Ihren Followern Inspiration direkt vom Ursprungsort gibt.",
    "You can find us in:": "Sie finden uns in:",
    "Slezská Ostrava": "Slezská Ostrava",
    "company headquarters": "Unternehmenszentrale",
    "Těrlicko": "Těrlicko",
    "production": "Produktion",
    "Ostrava - Hrabová": "Ostrava - Hrabová",
    "distribution warehouse": "Distributionslager",
    "Step 1/2 – Basic Information": "Schritt 1/2 – Grundlegende Informationen",
    "First Name *": "Vorname *",
    "Your first name": "Ihr Vorname",
    "Last Name *": "Nachname *",
    "Your last name": "Ihr Nachname",
    "E-mail *": "E-Mail *",
    "your@email.com": "ihre@email.de",
    "Phone *": "Telefon *",
    "+44 20 1234 5678": "+49 30 1234 5678",
    "I agree with the": "Ich stimme den",
    "terms of personal data processing": "Bedingungen zur Verarbeitung personenbezogener Daten zu",
    "I agree with the processing of personal data for marketing purposes": "Ich stimme der Verarbeitung personenbezogener Daten für Marketingzwecke zu",
    "Contact Me": "Kontaktieren Sie mich",
    "Your browser does not support the video element.": "Ihr Browser unterstützt das Videoelement nicht.",
    
    # Další sekce
    "Average monthly income of": "Durchschnittliches monatliches Einkommen von",
    "top 10 partners.": "Top 10 Partnern.",
    "BEWIT TRUE AFFILIATE – a new way to do business with heart. We combine the fairness of online affiliate with the natural principle of recommendation. When your recommendations spread – friends of your customers make purchases – the system rewards you automatically. No fees, no obligations, no manipulation. Just real value that keeps spreading.": "BEWIT TRUE AFFILIATE – eine neue Art, mit Herz Geschäfte zu machen. Wir kombinieren die Fairness des Online-Affiliate mit dem natürlichen Prinzip der Empfehlung. Wenn sich Ihre Empfehlungen verbreiten – Freunde Ihrer Kunden kaufen – belohnt Sie das System automatisch. Keine Gebühren, keine Verpflichtungen, keine Manipulation. Nur echter Wert, der sich weiter verbreitet.",
    "Of our partners earn over": "Unserer Partner verdienen über",
    "monthly": "monatlich",
    "Achieve earnings higher than £1,000 in traditional network marketing structures": "Erzielen Einnahmen von mehr als 1.000 £ in traditionellen Network-Marketing-Strukturen",
    "Work from anywhere – our system opens the path to customers around the world.": "Arbeiten Sie von überall – unser System öffnet den Weg zu Kunden auf der ganzen Welt.",
    
    # Why BEWIT is Different
    "No initial investment or purchase obligations – start without risk": "Keine Anfangsinvestition oder Kaufverpflichtungen – beginnen Sie ohne Risiko",
    "Offer online too – reach more people online with our free tools": "Bieten Sie auch online an – erreichen Sie mehr Menschen online mit unseren kostenlosen Tools",
    "Ethical products without chemicals, 100% plant-based – offer what you use yourself": "Ethische Produkte ohne Chemikalien, 100% pflanzlich – bieten Sie an, was Sie selbst verwenden",
    "No worries – no physical salon, no warehouse, no hassles": "Keine Sorgen – kein physischer Salon, kein Lager, keine Probleme",
    "Work from anywhere – from home or the beach, whatever suits you": "Arbeiten Sie von überall – von zu Hause oder vom Strand, wie es Ihnen passt",
    "Customers can buy without registration – no complications": "Kunden können ohne Registrierung kaufen – keine Komplikationen",
    "Strong brand with global reach – helps expand the network": "Starke Marke mit globaler Reichweite – hilft beim Ausbau des Netzwerks",
    "Yes, Start Earning": "Ja, beginnen Sie zu verdienen",
    
    # E-book sekce
    "Discover how to build a successful business with BEWIT – step by step": "Entdecken Sie, wie Sie ein erfolgreiches Geschäft mit BEWIT aufbauen – Schritt für Schritt",
    "Download a free e-book where you'll find a step-by-step explained system on how to work with BEWIT, earn a stable income, and build your own passive income.": "Laden Sie ein kostenloses E-Book herunter, in dem Sie ein Schritt-für-Schritt-erklärtes System finden, wie Sie mit BEWIT arbeiten, ein stabiles Einkommen erzielen und Ihr eigenes passives Einkommen aufbauen können.",
    
    # Kalkulačky
    "Your Potential Earnings": "Ihre potenziellen Einnahmen",
    "How much can you earn monthly?": "Wie viel können Sie monatlich verdienen?",
    "Number of sales per month:": "Anzahl der Verkäufe pro Monat:",
    "Your monthly commission:": "Ihre monatliche Provision:",
    "or": "oder",
    "How many customers do you need?": "Wie viele Kunden benötigen Sie?",
    "Desired monthly income:": "Gewünschtes monatliches Einkommen:",
    "You need approximately:": "Sie benötigen ungefähr:",
    "customers with average order value 1,200 CZK": "Kunden mit einem durchschnittlichen Bestellwert von 1.200 CZK",
    
    # Testimoniály
    "What Our Partners Say": "Was unsere Partner sagen",
    "Thanks to BEWIT, I earn extra income without leaving home. The products sell themselves because they really work!": "Dank BEWIT verdiene ich zusätzliches Einkommen, ohne das Haus zu verlassen. Die Produkte verkaufen sich von selbst, weil sie wirklich funktionieren!",
    "Partner since 2022 • Avg. 15,000 CZK/month": "Partner seit 2022 • Durchschn. 15.000 CZK/Monat",
    "I started with social media posts, today I have my own customer base and passive income I can rely on.": "Ich habe mit Social-Media-Posts begonnen, heute habe ich meinen eigenen Kundenstamm und passives Einkommen, auf das ich mich verlassen kann.",
    "Partner since 2021 • Avg. 8,000 CZK/month": "Partner seit 2021 • Durchschn. 8.000 CZK/Monat",
    "BEWIT is a safe bet – loyal customers keep coming back. For me, it's a welcome addition to my main income.": "BEWIT ist eine sichere Sache – treue Kunden kommen immer wieder. Für mich ist es eine willkommene Ergänzung zu meinem Haupteinkommen.",
    "Partner since 2023 • Avg. 20,000 CZK/month": "Partner seit 2023 • Durchschn. 20.000 CZK/Monat",
    "I was looking for something long-term, and I found it with BEWIT. I like that I don't have to keep inventory – everything is handled by the company.": "Ich suchte nach etwas Langfristigem und fand es bei BEWIT. Mir gefällt, dass ich kein Inventar führen muss – alles wird vom Unternehmen erledigt.",
    "Partner since 2020 • Avg. 12,000 CZK/month": "Partner seit 2020 • Durchschn. 12.000 CZK/Monat",
    
    # Úspěšnost
    "Our Partners' Success Rate": "Erfolgsquote unserer Partner",
    "Other MLM Programs": "Andere MLM-Programme",
    "Success Rate": "Erfolgsquote",
    "BEWIT Affiliate Program": "BEWIT-Partnerprogramm",
    "On average, our partners earn more than in traditional MLMs. Why? Because we don't require large stocks, minimum purchases, or recruiting new members.": "Im Durchschnitt verdienen unsere Partner mehr als in traditionellen MLMs. Warum? Weil wir keine großen Lagerbestände, Mindestkäufe oder die Anwerbung neuer Mitglieder verlangen.",
    
    # Mapa
    "Where Are We Heading?": "Wohin gehen wir?",
    "We've already established ourselves in Central Europe, and we're not stopping. Our goal is to expand to Western Europe and beyond. Join us on this journey – and share in the growth.": "Wir haben uns bereits in Mitteleuropa etabliert und hören nicht auf. Unser Ziel ist die Expansion nach Westeuropa und darüber hinaus. Begleiten Sie uns auf dieser Reise – und profitieren Sie vom Wachstum.",
    
    # Shrnutí
    "What You Get When You Join?": "Was erhalten Sie beim Beitritt?",
    "Up to 30% commission on every sale – from the 1st order": "Bis zu 30% Provision auf jeden Verkauf – ab der ersten Bestellung",
    "Access to marketing materials – banners, texts, graphics, product photos": "Zugang zu Marketingmaterialien – Banner, Texte, Grafiken, Produktfotos",
    "No obligation to purchase or maintain minimum stock": "Keine Verpflichtung zum Kauf oder zur Führung von Mindestbeständen",
    "No investment or membership fees": "Keine Investition oder Mitgliedschaftsgebühren",
    "Your own unique affiliate link – you can share it anywhere": "Ihr eigener einzigartiger Affiliate-Link – Sie können ihn überall teilen",
    "Personal support – we'll help you get started": "Persönliche Unterstützung – wir helfen Ihnen beim Einstieg",
    "Products customers love to return to – high quality with effect": "Produkte, zu denen Kunden gerne zurückkehren – hohe Qualität mit Wirkung",
    "Passive income – earn even from repeat purchases": "Passives Einkommen – verdienen Sie auch an Wiederholungskäufen",
    "Start Earning Today": "Beginnen Sie noch heute zu verdienen",
    
    # Formulář
    "Step 1/2 – We'll Get Back to You with an Offer": "Schritt 1/2 – Wir melden uns mit einem Angebot bei Ihnen",
    "Name": "Name",
    "Surname": "Nachname",
    "Email": "E-Mail",
    "Phone (with country code)": "Telefon (mit Landesvorwahl)",
    "Your region": "Ihre Region",
    "By submitting, I agree to the": "Mit der Absendung stimme ich den",
    "processing of personal data": "Verarbeitung personenbezogener Daten zu",
    "I agree to receive commercial communications and newsletters": "Ich stimme dem Erhalt von Werbekommunikation und Newslettern zu",
    "Continue to Step 2": "Weiter zu Schritt 2",
    
    # FAQ
    "Frequently Asked Questions": "Häufig gestellte Fragen",
    "How do I sign up?": "Wie kann ich mich anmelden?",
    "Simply fill out the form on this page. We'll send you an email with all the details and access to your affiliate account.": "Füllen Sie einfach das Formular auf dieser Seite aus. Wir senden Ihnen eine E-Mail mit allen Details und dem Zugang zu Ihrem Partner-Konto.",
    "How much does it cost?": "Wie viel kostet es?",
    "Nothing. Registration is completely free, and there are no hidden fees.": "Nichts. Die Registrierung ist völlig kostenlos und es gibt keine versteckten Gebühren.",
    "What commission do I get?": "Welche Provision erhalte ich?",
    "You get up to 30% commission on every sale made through your link.": "Sie erhalten bis zu 30% Provision auf jeden Verkauf, der über Ihren Link getätigt wird.",
    "Do I have to buy products or maintain inventory?": "Muss ich Produkte kaufen oder Inventar führen?",
    "No. You don't have to buy anything or keep stock. You simply share your link, and we handle everything else – shipping, payments, customer service.": "Nein. Sie müssen nichts kaufen oder Lagerbestände führen. Sie teilen einfach Ihren Link, und wir kümmern uns um alles andere – Versand, Zahlungen, Kundenservice.",
    "Can I share the link anywhere?": "Kann ich den Link überall teilen?",
    "Yes. On social media, your own website, blog, YouTube, via email, or directly with friends and family. Wherever you have an audience.": "Ja. In sozialen Medien, auf Ihrer eigenen Website, im Blog, auf YouTube, per E-Mail oder direkt mit Freunden und Familie. Überall dort, wo Sie ein Publikum haben.",
    "How and when do I get paid?": "Wie und wann werde ich bezahlt?",
    "Commission is paid monthly to the bank account you specify during registration.": "Die Provision wird monatlich auf das Bankkonto überwiesen, das Sie bei der Registrierung angeben.",
    "How long does the commission last?": "Wie lange dauert die Provision?",
    "Forever. Once a customer buys through your link, they become 'yours' – meaning you'll earn from all their future purchases too.": "Für immer. Sobald ein Kunde über Ihren Link kauft, wird er 'Ihrer' – das bedeutet, Sie verdienen auch an allen zukünftigen Käufen.",
    "What if I want to stop?": "Was ist, wenn ich aufhören möchte?",
    "You can stop anytime. There are no contracts or obligations.": "Sie können jederzeit aufhören. Es gibt keine Verträge oder Verpflichtungen.",
    
    # Patička
    "Contact": "Kontakt",
    "About Us": "Über uns",
    "Privacy Policy": "Datenschutzrichtlinie",
    
    # Thank you page
    "Thank You for Your Interest | Bewit Affiliate Program": "Vielen Dank für Ihr Interesse | Bewit-Partnerprogramm",
    "Thank you for your interest in the Bewit affiliate program. Please fill out a short questionnaire.": "Vielen Dank für Ihr Interesse am Bewit-Partnerprogramm. Bitte füllen Sie einen kurzen Fragebogen aus.",
    "Step 2/2 – About You and Cooperation": "Schritt 2/2 – Über Sie und die Zusammenarbeit",
    "Great. Just a few more details and we can start together!": "Großartig. Nur noch ein paar Details und wir können gemeinsam starten!",
    "To provide you with the best support, please tell us how you want to work with BEWIT. The form will only take 1–2 minutes.": "Um Ihnen die beste Unterstützung zu bieten, teilen Sie uns bitte mit, wie Sie mit BEWIT arbeiten möchten. Das Formular dauert nur 1–2 Minuten.",
    "For New Partners": "Für neue Partner",
    "Every partner is unique to us. That's why we'd like to know how you want to share BEWIT products and what we can do to make it easier for you. This way, we can prepare exactly the tools, support, and materials that will work best for you.": "Jeder Partner ist für uns einzigartig. Deshalb möchten wir wissen, wie Sie BEWIT-Produkte teilen möchten und was wir tun können, um es Ihnen zu erleichtern. So können wir genau die Werkzeuge, Unterstützung und Materialien vorbereiten, die für Sie am besten funktionieren.",
    "Tell us briefly about yourself?": "Erzählen Sie uns kurz über sich?",
    "e.g. what you do, what community you have, why BEWIT caught your attention…": "z.B. was Sie tun, welche Gemeinschaft Sie haben, warum BEWIT Ihre Aufmerksamkeit erregt hat…",
    "How big is your reach?": "Wie groß ist Ihre Reichweite?",
    "0-50 contacts": "0-50 Kontakte",
    "50-200 contacts": "50-200 Kontakte",
    "200-1000 contacts": "200-1000 Kontakte",
    "1000-5000 contacts": "1000-5000 Kontakte",
    "5000+ contacts": "5000+ Kontakte",
    "How do you want to share BEWIT products?": "Wie möchten Sie BEWIT-Produkte teilen?",
    "Social Media": "Soziale Medien",
    "Own Website": "Eigene Website",
    "Writing Articles": "Artikel schreiben",
    "YouTube": "YouTube",
    "Direct Sales": "Direktverkauf",
    "Other": "Andere",
    "Please specify how...": "Bitte geben Sie an, wie...",
    "Submit Form": "Formular absenden",
    "(After submitting the form, we will create your account and send you access credentials. We'll take care of everything else).": "(Nach dem Absenden des Formulars erstellen wir Ihr Konto und senden Ihnen die Zugangsdaten. Wir kümmern uns um alles Weitere).",
    "DONE": "FERTIG",
    "Thank you for filling out the questionnaire! We will contact you soon with more information.": "Vielen Dank für das Ausfüllen des Fragebogens! Wir werden uns bald mit weiteren Informationen bei Ihnen melden.",
    "Thank you for your interest!": "Vielen Dank für Ihr Interesse!",
    "Your questionnaire has been successfully submitted.": "Ihr Fragebogen wurde erfolgreich übermittelt.",
    "We will contact you soon with more information about the affiliate program.": "Wir werden uns bald mit weiteren Informationen zum Partnerprogramm bei Ihnen melden.",
    "An error occurred while submitting the questionnaire. Please try again.": "Beim Absenden des Fragebogens ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.",
    
    # Jazykový přepínač - labels
    "Čeština": "Tschechisch",
    "Slovenčina": "Slowakisch",
    "Polski": "Polnisch",
    "Magyar": "Ungarisch",
    "Română": "Rumänisch",
    "English": "Englisch",
    "Deutsch": "Deutsch",
}

def translate_html_file(input_file, output_file):
    """Přeloží HTML soubor z angličtiny do němčiny"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrahujeme CSS a JavaScript, abychom je nepřekládali
    style_pattern = r'(<style>.*?</style>)'
    script_pattern = r'(<script>.*?</script>)'
    
    styles = re.findall(style_pattern, content, re.DOTALL)
    scripts = re.findall(script_pattern, content, re.DOTALL)
    
    # Nahradíme CSS a JS placeholdery
    for i, style in enumerate(styles):
        content = content.replace(style, f'___STYLE_PLACEHOLDER_{i}___')
    
    for i, script in enumerate(scripts):
        content = content.replace(script, f'___SCRIPT_PLACEHOLDER_{i}___')
    
    # Překlad meta tagů a textu (pouze HTML obsah)
    # Používáme word boundaries a kontrolujeme kontext, aby se nepřepisovaly HTML atributy
    for en_text, de_text in translations.items():
        # Pro krátká slova (name, color, form, storage, or) použijeme přesnější matching
        if len(en_text.split()) == 1 and len(en_text) <= 7:
            # Přeložíme pouze když je to celé slovo v textu, ne v atributech
            # Použijeme lookahead a lookbehind pro kontrolu kontextu
            pattern = r'(?<=[>"\s])' + re.escape(en_text) + r'(?=[<"\s])'
            content = re.sub(pattern, de_text, content, flags=re.IGNORECASE)
        else:
            # Pro delší fráze použijeme normální překlad
            en_escaped = re.escape(en_text)
            content = re.sub(en_escaped, de_text, content, flags=re.IGNORECASE)
    
    # Změna lang atributu
    content = content.replace('lang="en"', 'lang="de"')
    
    # Úprava hreflang tagů - přidání DE
    if 'hreflang="en"' in content:
        # Najdeme poslední hreflang tag před x-default
        x_default_pattern = r'(<link rel="alternate" hreflang="x-default"[^>]*>)'
        
        # Přidáme DE hreflang před x-default
        de_hreflang = '    <link rel="alternate" hreflang="de" href="https://bewit.love/de/Afill_MLM/">\n'
        de_hreflang_thankyou = '    <link rel="alternate" hreflang="de" href="https://bewit.love/de/Afill_MLM/thank-you.html">\n'
        
        if 'thank-you.html' in content:
            content = re.sub(x_default_pattern, de_hreflang_thankyou + r'\1', content)
        else:
            content = re.sub(x_default_pattern, de_hreflang + r'\1', content)
    
    # Úprava canonical URL
    content = content.replace('href="https://bewit.love/en/Afill_MLM/', 'href="https://bewit.love/de/Afill_MLM/')
    
    # Úprava OG URL
    content = content.replace('content="https://bewit.love/en/Afill_MLM/', 'content="https://bewit.love/de/Afill_MLM/')
    
    # Úprava og:locale
    content = content.replace('content="en_US"', 'content="de_DE"')
    
    # Úprava jazykového přepínače - přidání DE a označení jako active
    if 'language-options' in content:
        # Přidáme DE do jazykového přepínače
        de_option = '                <a href="../de/thank-you.html" class="active" title="Deutsch">🇩🇪 Deutsch</a>\n'
        de_option_index = '                <a href="../de/" class="active" title="Deutsch">🇩🇪 Deutsch</a>\n'
        
        # Odstraníme active z EN
        content = content.replace('<a href="../en/thank-you.html" class="active"', '<a href="../en/thank-you.html"')
        content = content.replace('<a href="../en/" class="active"', '<a href="../en/"')
        
        # Přidáme DE před EN
        if 'thank-you.html' in content:
            content = content.replace(
                '                <a href="../en/thank-you.html"',
                de_option + '                <a href="../en/thank-you.html"'
            )
        else:
            content = content.replace(
                '                <a href="../en/"',
                de_option_index + '                <a href="../en/"'
            )
    
    # Změna vlajky v language-current na DE
    if 'language-current' in content:
        # Najdeme sekci language-current a změníme vlajku
        content = re.sub(
            r'(<div class="language-current"[^>]*>\s*<span>)🇬🇧(</span>)',
            r'\1🇩🇪\2',
            content
        )
    
    # Úprava odkazů v jazykovém přepínači
    if 'thank-you.html' in content:
        # Thank you page
        pass  # odkazy jsou už správně relativní
    else:
        # Index page
        pass  # odkazy jsou už správně relativní
    
    # Vrátíme CSS a JS na místo
    for i, style in enumerate(styles):
        content = content.replace(f'___STYLE_PLACEHOLDER_{i}___', style)
    
    for i, script in enumerate(scripts):
        # Upravíme country parametr v JS
        script_modified = script.replace("data.country = 'EN';", "data.country = 'DE';")
        
        # Přidáme DE do langMap
        if 'const langMap' in script_modified:
            if 'thank-you.html' in input_file:
                # Pro thank-you.html
                script_modified = script_modified.replace(
                    "'ro': '../ro/thank-you.html'",
                    "'ro': '../ro/thank-you.html',\n            'de': '../de/thank-you.html'"
                )
            else:
                # Pro index.html
                script_modified = script_modified.replace(
                    "'ro': '../ro/index.html'",
                    "'ro': '../ro/index.html',\n            'de': '../de/index.html'"
                )
        
        content = content.replace(f'___SCRIPT_PLACEHOLDER_{i}___', script_modified)
    
    # Úprava auto-redirect skriptu už není potřeba, protože JS je teď zpět
    
    # Uložení
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Přeloženo: {output_file}")

def main():
    """Hlavní funkce"""
    print("🚀 Začínám překlad do němčiny (DE)...")
    
    # Překlad index.html
    translate_html_file(
        '/Users/petrhajduk/Documents/Code/Bewit/Affiliate_1/Afill_MLM/en/index.html',
        '/Users/petrhajduk/Documents/Code/Bewit/Affiliate_1/Afill_MLM/de/index.html'
    )
    
    # Překlad thank-you.html
    translate_html_file(
        '/Users/petrhajduk/Documents/Code/Bewit/Affiliate_1/Afill_MLM/en/thank-you.html',
        '/Users/petrhajduk/Documents/Code/Bewit/Affiliate_1/Afill_MLM/de/thank-you.html'
    )
    
    print("\n✨ Překlad dokončen!")
    print("📁 Vytvořené soubory:")
    print("   - de/index.html")
    print("   - de/thank-you.html")

if __name__ == "__main__":
    main()
