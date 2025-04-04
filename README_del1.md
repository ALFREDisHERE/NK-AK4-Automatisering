
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

## ⚠️ Før du bruker skriptet – viktig å vite:

### Kjør kun én endring per skript-session
- Du kan **ikke gjøre flere endringer i samme kjøring** av skriptet.
  - Eksempel: Hvis du konfigurerer SSH, må du kjøre skriptet på nytt for å gjøre VLAN- eller port-endringer.
  - Dette gjelder også dersom du skal endre **flere porter** eller **flere VLAN-er** – én ting av gangen!
- **Kort oppsummert:** Hver gang du skal gjøre en ny endring, kjør skriptet på nytt og svar `skip` på alle de andre spørsmålene.

---

### Sjekk at enheten ikke står i global config mode
- Gå inn på enheten manuelt og sørg for at den ikke er i global config (`Switch(config)#`).
- Hvis den er det, skriv `no` for å gå ut og vent noen sekunder før du kjører skriptet.

---

### Ikke ha PuTTY åpen samtidig
- Du kan **ikke ha en PuTTY-tilkobling oppe på samme COM-port** samtidig som skriptet kjører.
- Lukk PuTTY helt hvis du bruker den samme COM-porten som skriptet skal koble seg til.

---

### Start alltid i pre-enable prompt
- Det skal stå noe som `Switch>` eller `Router>` i konsollen, altså **ikke** `Switch#` eller `Router(config)#`.
- Det **kan fungere** uten dette, men det er tryggest å begynne her.

---

### Hvis skriptet "henger"
- Noen ganger venter enheten på brukernavn eller passord i det som kan kalles en "pre-default state".
- I så fall må du koble til via serial og trykke `Enter` én gang – da kommer den i riktig tilstand.

---

### Se video
- Hvis du står fast, se **demovideoen nederst i README** der jeg viser hvordan jeg satte opp RR2.
  - Legg merke til når jeg **skipper** steg og når jeg **kjører skriptet på nytt**.

---

### For dypere innsikt
- Alle skript er kommentert – se kommentarene i koden for forklaringer på hva som skjer og hvorfor.


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

