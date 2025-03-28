# NK-AK4-Automatisering

Konfigureringsskript for Nettverksenheter

Dette prosjektet inneholder et Python-skript for å konfigurere nettverksenheter via en seriell tilkobling. Skriptet kan brukes til å sette opp SSH, konfigurere porter og opprette VLAN.

Funksjonalitet

SSH-konfigurasjon: Oppretter hostname, domene, RSA-nøkkel, og brukerkonto.

Portkonfigurasjon: Støtte for ruter- og switchporter.

VLAN-konfigurasjon: Oppretter VLAN, tildeler IP-adresser og setter opp default gateway.

Installasjon

Klon dette repoet:

git clone https://github.com/dittbrukernavn/nettverkskonfig.git
cd nettverkskonfig

Installer nødvendige Python-avhengigheter:

pip install pyserial

Bruk

Koble til enheten via en seriell port.

Kjør skriptet:

python konfigurasjon.py

Følg instruksjonene for å sette opp SSH, porter og VLAN.
