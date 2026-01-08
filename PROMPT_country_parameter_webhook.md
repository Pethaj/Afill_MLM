# PROMPT: Přidání parametru "country" do webhooků ve funnelu

## 🎯 Úkol
Přidej do všech formulářů na všech jazykových mutacích tohoto funnelu parametr **`country`**, který bude obsahovat kód země (CZ/SK/PL/HU/RO) podle toho, na které jazykové mutaci uživatel vyplnil formulář.

## 📋 Požadavky

### 1. Jazykové mutace, které je třeba upravit:
- **CZ verze** (hlavní): `/index.html`
- **SK verze**: `/sk/index.html`
- **PL verze**: `/pl/index.html`
- **HU verze**: `/hu/index.html`
- **RO verze**: `/ro/index.html`

### 2. Formuláře, které je třeba upravit v KAŽDÉ mutaci:
- ✅ Všechny formuláře, které odesílají data na webhook
- ✅ Typicky to jsou: registrační formuláře, kontaktní formuláře, lead formuláře apod.

---

## 🔧 Implementace

### Pro ČESKOU verzi (`/index.html`):

Ve všech formulářích, kde se připravují data pro webhook (`webhookData` nebo podobný objekt), přidej:

**Krok 1:** Před přípravu dat pro webhook přidej funkci pro detekci země:

```javascript
// Detekce jazykové mutace z URL cesty
const getCountryFromUrl = () => {
    const path = window.location.pathname;
    if (path.includes('/sk/')) return 'SK';
    if (path.includes('/pl/')) return 'PL';
    if (path.includes('/hu/')) return 'HU';
    if (path.includes('/ro/')) return 'RO';
    return 'CZ'; // výchozí
};
```

**Krok 2:** Do objektu s daty pro webhook přidej:

```javascript
const webhookData = {
    // ... ostatní existující data ...
    
    // Jazyková mutace / Země
    country: getCountryFromUrl(),
    
    // ... další existující data ...
};
```

### Pro SLOVENSKOU verzi (`/sk/index.html`):

Do objektu s daty pro webhook přidej (natvrdo):

```javascript
const webhookData = {
    // ... ostatní existující data ...
    
    country: 'SK',
    
    // ... další existující data ...
};
```

### Pro POLSKOU verzi (`/pl/index.html`):

Do objektu s daty pro webhook přidej (natvrdo):

```javascript
const webhookData = {
    // ... ostatní existující data ...
    
    country: 'PL',
    
    // ... další existující data ...
};
```

### Pro MAĎARSKOU verzi (`/hu/index.html`):

Do objektu s daty pro webhook přidej (natvrdo):

```javascript
const webhookData = {
    // ... ostatní existující data ...
    
    country: 'HU',
    
    // ... další existující data ...
};
```

### Pro RUMUNSKOU verzi (`/ro/index.html`):

Do objektu s daty pro webhook přidej (natvrdo):

```javascript
const webhookData = {
    // ... ostatní existující data ...
    
    country: 'RO',
    
    // ... další existující data ...
};
```

---

## 📍 Kde přesně to najít a upravit?

1. **Otevři soubor** (např. `/index.html`)
2. **Vyhledej** text: `webhook` nebo `webhookData` nebo `prepareWebhookData`
3. **Najdi** místo, kde se připravují data pro odeslání na webhook (obvykle objekt s daty z formuláře)
4. **Přidej** parametr `country` podle výše uvedených instrukcí

### Příklad PŘED úpravou:

```javascript
const webhookData = {
    customerId: customerId,
    firstName: firstName,
    lastName: lastName,
    email: email,
    phone: phone,
    // ... další data ...
    timestamp: new Date().toISOString(),
};
```

### Příklad PO úpravě (CZ verze):

```javascript
// Detekce jazykové mutace z URL cesty
const getCountryFromUrl = () => {
    const path = window.location.pathname;
    if (path.includes('/sk/')) return 'SK';
    if (path.includes('/pl/')) return 'PL';
    if (path.includes('/hu/')) return 'HU';
    if (path.includes('/ro/')) return 'RO';
    return 'CZ'; // výchozí
};

const webhookData = {
    customerId: customerId,
    firstName: firstName,
    lastName: lastName,
    email: email,
    phone: phone,
    // ... další data ...
    
    // Jazyková mutace / Země
    country: getCountryFromUrl(),
    
    timestamp: new Date().toISOString(),
};
```

### Příklad PO úpravě (SK/PL/HU/RO verze):

```javascript
const webhookData = {
    customerId: customerId,
    firstName: firstName,
    lastName: lastName,
    email: email,
    phone: phone,
    // ... další data ...
    
    country: 'SK',  // nebo 'PL', 'HU', 'RO' podle jazykové mutace
    
    timestamp: new Date().toISOString(),
};
```

---

## ✅ Kontrola

Po dokončení implementace:

1. ✅ Zkontroluj, že **každý soubor** (index.html) má úpravu
2. ✅ Zkontroluj, že **každý formulář** v daném souboru má přidán parametr `country`
3. ✅ Zkontroluj správné kódy zemí:
   - CZ verze: dynamická detekce nebo 'CZ'
   - SK verze: 'SK'
   - PL verze: 'PL'
   - HU verze: 'HU'
   - RO verze: 'RO'

---

## 🌍 Výsledný webhook data

Po implementaci bude webhook dostávat data ve struktuře:

```json
{
    "customerId": "abc123",
    "firstName": "János",
    "lastName": "Kovács",
    "email": "janos@example.com",
    "phone": "+36301234567",
    "country": "HU",
    "privacyConsent": true,
    "marketingConsent": true,
    "timestamp": "2025-12-01T10:30:00.000Z",
    "source": "registration_form",
    "url": "https://example.com/hu/index.html"
}
```

---

## 🚀 Použití promptu

**Zkopíruj tento text a použij:**

```
Přidej do všech formulářů na všech jazykových mutacích parametr "country" do webhooku.

Struktura funnelu:
- CZ verze: /index.html
- SK verze: /sk/index.html  
- PL verze: /pl/index.html
- HU verze: /hu/index.html
- RO verze: /ro/index.html

Pro CZ verzi použij dynamickou detekci z URL:
const getCountryFromUrl = () => {
    const path = window.location.pathname;
    if (path.includes('/sk/')) return 'SK';
    if (path.includes('/pl/')) return 'PL';
    if (path.includes('/hu/')) return 'HU';
    if (path.includes('/ro/')) return 'RO';
    return 'CZ';
};

A přidej do webhookData:
country: getCountryFromUrl(),

Pro ostatní jazykové mutace přidej natvrdo:
- SK: country: 'SK',
- PL: country: 'PL',
- HU: country: 'HU',
- RO: country: 'RO',

Uprav všechny formuláře, které odesílají data na webhook ve všech 5 jazykových mutacích.
```

---

## 📝 Poznámky

- Parametr se přidává do VŠECH formulářů, které odesílají webhook
- U CZ verze je detekce dynamická (pro případ, že někdo otevře např. SK verzi přímo)
- U ostatních mutací je kód země natvrdo (jednodušší a spolehlivější)
- Parametr se umísťuje mezi data formuláře a metadata (timestamp apod.)
- Pojmenování: `country` (anglicky, protože webhook může jít na mezinárodní systémy)

---

## 🔄 Verze

- Vytvořeno: 1.12.2025
- Testováno na: Afill_MLM funnel
- Status: ✅ Produkční


