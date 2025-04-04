
# Konfigureringsskript for Nettverksenheter - NK-AK4-Automatisering

Python-skript for å konfigurere nettverksenheter via en en com kabel

## Funksjonalitet
- **SSH-konfigurasjon**: Oppretter hostname, domene, RSA-nøkkel, og brukerkonto.
- **Portkonfigurasjon**: Støtte for ruter- og switchporter.
- **VLAN-konfigurasjon**: Oppretter VLAN, tildeler IP-adresser og setter opp default gateway.

## Installasjon
1. Klon dette repoet:
   ```bash
   git clone https://github.com/ALFREDisHERE/NK-AK4-Automatisering
   cd nettverkskonfig
   ```
2. Installer nødvendige Python-avhengigheter:
   ```bash
   pip install pyserial
   ```

## Bruk
Koble til enheten via en com port.
Om du ikke hvet hva comport den bruker kan du trykke Win+X>enhetsbehandling>porter(com og LPT) der finner du liste over alle tilgjenglige com porter som du kan bruke. 
Antall porter varierer veldig fra pc til pc.

## For å bruke skriptet må du vite noen ting først:
- du kan ikke gjøre flere endringer på samme session av skriptet
  -- eksempel: om du kjører det og setter opp ssh så kan du ikke gjøre noen port/vlan endringer i samme session, så da må du kjøre skriptet igjen å velge nei på ssh og da gjøre endringer på port eller vlan.
  -- dette gjelder også 2 porter, 2 vlan, osv
  -- kort forklart. bare kjør skriptet hver gang du skal konfiguere noe og skriv skip på alt anna.
-du må gå inn på enheten å forsikre deg at den ikke står å venter på global configuration. om den gjør det skriv no og vent noen minutter.
-du kan ikke ha oppe en putty session på samme comport samtidg som skriptet kjøres
-pass på at den er på pre enable planet i startet
-- eksempel: det må stå switch> eller router> eller noe lignene i konsollen (helst uten at den er enabled altså der er e #)
-- det funker av og til uten om dette men det er best å være på den sikre siden.
-- det er av og til den står i det jeg liker å kalle pre default planet der den står å venter på input på bruker, jeg har prøvd å sende en empty command som sender bare enter men det funket ikke, så om ingen endringer skjer kan du koble til over serial og trykke enter en gang :D.
- om du sitter fast kan du se demovideoen nedenfor som demostrerer hvordan jeg satt opp RR2 (en ruter) legg merke til når jeg skipper og når jeg kjører skriptet på nytt.
- for dypere forklaring av koden sjekk kommentarene i skriptet

Kjør skriptet:
   ```bash
   python ./ak4_ssh_ver11.py
   ```
Følg instruksjonene for å sette opp SSH, konfiguere porter og VLAN.

## Krav
- Python 3
- `pyserial`
- En cisco-enhet med en com tilkobling

Demo Video

https://github.com/user-attachments/assets/2e522031-380f-4253-be28-b8af3ec9ca20

