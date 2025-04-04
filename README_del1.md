
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
1. Koble til enheten via en com port.
2. Kjør skriptet:
   ```bash
   python ./ak4_ssh_ver10.py
   ```
3. Følg instruksjonene for å sette opp SSH, konfiguere porter og VLAN.

## Krav
- Python 3
- `pyserial`
- En ciscoenhet med en com tilkobling

Demo Video

https://github.com/user-attachments/assets/2e522031-380f-4253-be28-b8af3ec9ca20

